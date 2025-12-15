"""
Email Reply Webhook
Receives email replies from SendGrid Inbound Parse.
Parses selection and triggers Cloud Run job.
"""

import functions_framework
import json
import os
import re
from datetime import datetime
from google.cloud import storage
import requests

# Configuration
GCS_BUCKET = os.environ.get("GCS_BUCKET")
PROJECT_ID = os.environ.get("GCP_PROJECT")
REGION = os.environ.get("GCP_REGION", "us-central1")
JOB_NAME = "podcast-processor"
AUTHORIZED_EMAILS = os.environ.get("AUTHORIZED_EMAILS", "altmbr@gmail.com").split(",")
TEST_MODE = os.environ.get("TEST_MODE", "true").lower() == "true"


def parse_sender_email(from_header):
    """Extract email address from From header."""
    match = re.search(r'[\w\.-]+@[\w\.-]+', from_header)
    return match.group(0).lower() if match else None


def get_clean_body(text):
    """Get clean email body (remove quoted text, signatures)."""
    lines = text.strip().split('\n')

    # Take only lines before "On ... wrote:" or similar
    clean_lines = []
    for line in lines:
        if re.match(r'^On .+ wrote:', line):
            break
        if line.strip().startswith('>'):
            continue
        clean_lines.append(line)

    return '\n'.join(clean_lines)


def parse_selection(text):
    """Parse selection from email body."""
    body = get_clean_body(text).lower()

    # Parse selection
    if 'all' in body:
        return 'all'
    if 'none' in body or 'cancel' in body:
        return 'none'

    # Look for numbers like "1,2,3" or "1, 3, 5" or "1 3 5"
    # But exclude numbers that are part of URLs
    body_without_urls = re.sub(r'https?://\S+', '', body)
    numbers = re.findall(r'\d+', body_without_urls)
    if numbers:
        return [int(n) for n in numbers]

    return None


def parse_oneoff_urls(text):
    """Extract one-off YouTube URLs from email body."""
    body = get_clean_body(text)

    # Find all YouTube URLs
    youtube_patterns = [
        r'https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'https?://youtu\.be/[\w-]+',
        r'https?://(?:www\.)?youtube\.com/shorts/[\w-]+',
    ]

    urls = []
    for pattern in youtube_patterns:
        urls.extend(re.findall(pattern, body))

    # Deduplicate while preserving order
    seen = set()
    unique_urls = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)

    return unique_urls


def extract_video_id(url):
    """Extract video ID from YouTube URL."""
    patterns = [
        r'youtube\.com/watch\?v=([\w-]+)',
        r'youtu\.be/([\w-]+)',
        r'youtube\.com/shorts/([\w-]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def extract_session_id(text):
    """Extract session ID from email body."""
    match = re.search(r'Session:\s*(sess_\w+)', text)
    return match.group(1) if match else None


def load_pending_session(session_id):
    """Load pending session from Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)
    blob = bucket.blob(f"pending_sessions/{session_id}.json")

    if not blob.exists():
        return None

    return json.loads(blob.download_as_text())


def save_selection_history(session_data, selection, selected_episodes, rejected_episodes):
    """Append selection to history for ML training."""
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)

    # Load existing history
    history_blob = bucket.blob("selection_history.json")
    if history_blob.exists():
        history = json.loads(history_blob.download_as_text())
    else:
        history = {"version": "1.0", "selections": []}

    # Calculate response time
    created_at = datetime.fromisoformat(session_data["created_at"].replace("Z", "+00:00"))
    response_time = (datetime.utcnow().replace(tzinfo=created_at.tzinfo) - created_at).total_seconds() / 60

    # Build selection record
    record = {
        "session_id": session_data["session_id"],
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "response_time_minutes": round(response_time, 1),
        "total_episodes_presented": len(session_data["episodes"]),
        "total_episodes_selected": len(selected_episodes),
        "selection_input": str(selection),
        "selected": selected_episodes,
        "rejected": rejected_episodes
    }

    history["selections"].append(record)

    # Save updated history
    history_blob.upload_from_string(json.dumps(history, indent=2))

    print(f"Saved selection: {len(selected_episodes)} selected, {len(rejected_episodes)} rejected")


def trigger_cloud_run_job(episodes):
    """Trigger Cloud Run job to process episodes."""
    # For now, we'll use gcloud command via Cloud Run API
    # In production, use the Cloud Run Admin API client library

    print(f"Would trigger Cloud Run job with {len(episodes)} episode(s)")
    print(f"Job: {PROJECT_ID}/{REGION}/{JOB_NAME}")

    # TODO: Implement actual Cloud Run job trigger using google-cloud-run library
    # For now, log the episodes that would be processed
    for ep in episodes:
        print(f"  - {ep['title']}")

    return "job-execution-simulated"


@functions_framework.http
def webhook(request):
    """Main entry point for email webhook."""

    print("Webhook received")

    # Parse incoming email from SendGrid
    from_email = parse_sender_email(request.form.get('from', ''))
    subject = request.form.get('subject', '')
    text = request.form.get('text', '')

    print(f"From: {from_email}")
    print(f"Subject: {subject}")
    print(f"Body preview: {text[:200]}...")

    # Verify sender
    if from_email not in [e.lower() for e in AUTHORIZED_EMAILS]:
        print(f"Unauthorized sender: {from_email}")
        return {"status": "error", "message": "Unauthorized"}, 403

    # Parse one-off URLs first
    oneoff_urls = parse_oneoff_urls(text)
    oneoff_episodes = []
    if oneoff_urls:
        print(f"Found {len(oneoff_urls)} one-off URL(s)")
        for url in oneoff_urls:
            video_id = extract_video_id(url)
            if video_id:
                oneoff_episodes.append({
                    "video_id": video_id,
                    "video_url": url,
                    "title": f"One-off: {video_id}",  # Title will be fetched during processing
                    "podcast_name": "one-off-episodes",
                    "podcast_url": "one-off-episodes",
                    "upload_date": None,
                    "is_oneoff": True
                })
                print(f"  - Added one-off: {video_id}")

    # Parse selection from numbered list
    selection = parse_selection(text)
    print(f"Parsed selection: {selection}")

    # Extract session ID
    session_id = extract_session_id(text)

    # Initialize lists
    selected_episodes = []
    rejected_episodes = []

    # If we have a session, process selections from the list
    if session_id:
        session_data = load_pending_session(session_id)
        if session_data:
            episodes = session_data["episodes"]

            # Determine selected and rejected episodes from the list
            if selection == 'all':
                selected_episodes = episodes.copy()
                rejected_episodes = []
            elif selection == 'none':
                selected_episodes = []
                rejected_episodes = episodes.copy()
            elif selection:
                # selection is list of indices (1-based)
                selected_episodes = [episodes[i-1] for i in selection if 0 < i <= len(episodes)]
                selected_indices = set(selection)
                rejected_episodes = [ep for i, ep in enumerate(episodes, 1) if i not in selected_indices]

            # Save selection history (for ML training)
            save_selection_history(session_data, selection, selected_episodes, rejected_episodes)
        else:
            print(f"Session not found: {session_id}")
    else:
        print("No session ID found (might be one-off only)")

    # Add one-off episodes to selected list
    if oneoff_episodes:
        selected_episodes.extend(oneoff_episodes)
        print(f"Added {len(oneoff_episodes)} one-off episode(s) to selection")

    # If nothing to process
    if not selected_episodes:
        if not oneoff_urls and selection is None:
            return {"status": "error", "message": "Could not parse selection or URLs"}, 400
        return {
            "status": "ok",
            "message": "No episodes selected",
            "rejected": len(rejected_episodes)
        }

    # Trigger processing
    if not TEST_MODE:
        job_id = trigger_cloud_run_job(selected_episodes)
        return {
            "status": "ok",
            "message": f"Processing {len(selected_episodes)} episode(s)",
            "job_id": job_id,
            "selected": len(selected_episodes),
            "oneoff": len(oneoff_episodes),
            "rejected": len(rejected_episodes)
        }
    else:
        print(f"TEST MODE: Would process {len(selected_episodes)} episode(s)")
        return {
            "status": "ok",
            "message": "TEST MODE - No processing triggered",
            "test_mode": True,
            "would_process": len(selected_episodes),
            "oneoff": len(oneoff_episodes),
            "rejected": len(rejected_episodes)
        }
