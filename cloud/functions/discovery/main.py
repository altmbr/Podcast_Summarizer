"""
Discovery Cloud Function
Scans for new episodes and sends selection email.
Triggered by Cloud Scheduler at 1 PM EST daily.
"""

import functions_framework
import json
import os
import re
import uuid
from datetime import datetime, timedelta
from google.cloud import storage
import requests

# Configuration
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/altmbr/Podcast_Summarizer/main"
GCS_BUCKET = os.environ.get("GCS_BUCKET")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
TEST_MODE = os.environ.get("TEST_MODE", "true").lower() == "true"
TEST_EMAIL = os.environ.get("TEST_EMAIL", "altmbr@gmail.com")
RECIPIENT_EMAIL = TEST_EMAIL if TEST_MODE else "altmbr@gmail.com"


def fetch_podcast_status():
    """Fetch current podcast_status.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/podcast_status.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def is_recent_episode(upload_date, days=2):
    """Check if episode was uploaded within the specified days."""
    if not upload_date:
        return False

    try:
        # Parse YYYYMMDD format
        if len(upload_date) == 8:
            episode_date = datetime.strptime(upload_date, "%Y%m%d").date()
        else:
            return False

        # Check if within specified days (compare dates only, not datetime)
        today = datetime.utcnow().date()
        cutoff = today - timedelta(days=days)
        return episode_date >= cutoff
    except:
        return False


def fetch_new_episodes(status_data):
    """Find incomplete episodes (not yet summarized) from the past 48 hours."""
    new_episodes = []
    incomplete_statuses = ['discovered', 'downloaded', 'transcribed']

    for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
        podcast_name = podcast_data.get("podcast_name", "Unknown")

        for video_id, episode_data in podcast_data.get("episodes", {}).items():
            status = episode_data.get("status")

            # Include any incomplete episode (not yet summarized)
            if status in incomplete_statuses:
                upload_date = episode_data.get("upload_date")

                # Only include episodes from past 3 days
                if is_recent_episode(upload_date, days=3):
                    new_episodes.append({
                        "podcast_name": podcast_name,
                        "podcast_url": podcast_url,
                        "title": episode_data.get("title", "Unknown"),
                        "video_id": video_id,
                        "video_url": f"https://youtube.com/watch?v={video_id}",
                        "upload_date": upload_date,
                        "region": episode_data.get("region", "Western"),
                        "duration_seconds": episode_data.get("duration_seconds"),
                        "status": status,
                    })

    # Sort by upload_date descending
    new_episodes.sort(key=lambda x: x.get("upload_date", "0"), reverse=True)
    return new_episodes


def estimate_cost(episode):
    """Estimate processing cost for an episode."""
    duration_hours = (episode.get("duration_seconds") or 3600) / 3600
    # CPU processing: slower, more expensive compute time
    cpu_cost = duration_hours * 2 * 0.10  # ~2x realtime on CPU, $0.10/hr compute
    claude_cost = 0.35 + (duration_hours * 0.5)  # Base + per-hour estimate
    return round(cpu_cost + claude_cost, 2)


def format_duration(seconds):
    """Format seconds as human-readable duration."""
    if not seconds:
        return "Unknown"
    hours, remainder = divmod(int(seconds), 3600)
    minutes, _ = divmod(remainder, 60)
    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def save_pending_session(session_id, episodes):
    """Save pending session to Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(f"pending_sessions/{session_id}.json")

    data = {
        "session_id": session_id,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "episodes": episodes
    }

    blob.upload_from_string(json.dumps(data, indent=2))


def send_discovery_email(episodes, session_id):
    """Send discovery email with episode list."""

    # Build HTML email body
    html_lines = ["<html><body>"]

    if TEST_MODE:
        html_lines.append("<p><strong>⚠️ TEST MODE - Only sending to test email</strong></p>")

    html_lines.append("<h2>Incomplete episodes (past 3 days):</h2>")
    html_lines.append("<ol>")

    # Status emoji mapping
    status_icons = {
        "discovered": "🔍",
        "downloaded": "⬇️",
        "transcribed": "📝"
    }

    total_cost = 0
    for i, ep in enumerate(episodes, 1):
        cost = estimate_cost(ep)
        total_cost += cost
        duration = format_duration(ep.get("duration_seconds"))
        upload_date = ep.get("upload_date", "Unknown")
        if upload_date and len(upload_date) == 8:
            upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
        status_icon = status_icons.get(ep.get("status", "discovered"), "🔍")

        html_lines.append(
            f"<li>{status_icon} <strong>[{ep['podcast_name']}]</strong> {ep['title']}<br/>"
            f"<small>Published: {upload_date} | Duration: {duration} | Est. cost: ${cost:.2f}</small></li>"
        )

    html_lines.append("</ol>")
    html_lines.append(f"<p><strong>Total estimated cost: ${total_cost:.2f}</strong></p>")

    # Clear instructions section
    html_lines.append("<hr/>")
    html_lines.append("<h3>How to Reply:</h3>")
    html_lines.append("<p><strong>Select episodes from list above:</strong></p>")
    html_lines.append("<ul>")
    html_lines.append("<li><code>all</code> - process all episodes</li>")
    html_lines.append("<li><code>1,2,3</code> - process specific episodes by number</li>")
    html_lines.append("<li><code>none</code> - skip all episodes</li>")
    html_lines.append("</ul>")
    html_lines.append("<p><strong>Add one-off episodes (paste URLs on separate lines):</strong></p>")
    html_lines.append("<pre>")
    html_lines.append("URLS:")
    html_lines.append("https://youtube.com/watch?v=xxxxx")
    html_lines.append("https://youtube.com/watch?v=yyyyy")
    html_lines.append("</pre>")
    html_lines.append("<p><small>You can combine both: select from list AND add URLs in same reply.</small></p>")
    html_lines.append("<hr/>")
    html_lines.append(f"<p><small>Session: {session_id}</small></p>")
    html_lines.append("</body></html>")

    html_body = "\n".join(html_lines)

    # Send via SendGrid
    response = requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "personalizations": [{"to": [{"email": RECIPIENT_EMAIL}]}],
            "from": {"email": "discovery@teahose.com", "name": "Podcast Discovery"},
            "reply_to": {"email": "reply@teahose.com"},
            "subject": f"{len(episodes)} new episodes ready to process",
            "content": [{"type": "text/html", "value": html_body}]
        }
    )

    return response.status_code == 202


@functions_framework.http
def discovery(request):
    """Main entry point for discovery function."""

    print(f"Discovery function triggered. TEST_MODE={TEST_MODE}")

    try:
        # Fetch current status
        status_data = fetch_podcast_status()

        # Find new episodes
        new_episodes = fetch_new_episodes(status_data)

        if not new_episodes:
            print("No new episodes found")
            return {"status": "ok", "message": "No new episodes", "count": 0}

        print(f"Found {len(new_episodes)} new episode(s)")

        # Generate session ID
        session_id = f"sess_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"

        # Save pending session
        save_pending_session(session_id, new_episodes)

        # Send email
        email_sent = send_discovery_email(new_episodes, session_id)

        return {
            "status": "ok",
            "message": "Discovery email sent" if email_sent else "Failed to send email",
            "count": len(new_episodes),
            "session_id": session_id,
            "test_mode": TEST_MODE
        }

    except Exception as e:
        print(f"Error in discovery: {e}")
        import traceback
        traceback.print_exc()
        return {"status": "error", "message": str(e)}, 500
