"""
Podscan Processor Cloud Function
Fully automated: discover new episodes via Podscan API, summarize with Claude, push to git.
Triggered by Cloud Scheduler daily at 1 PM EST.
"""

import functions_framework
import json
import os
import re
import tempfile
import time
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from anthropic import Anthropic
from git import Repo


# Configuration
PODSCAN_API_KEY = os.environ.get("PODSCAN_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", "altmbr@gmail.com")
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/altmbr/Podcast_Summarizer/main"
LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS", "3"))

PODSCAN_BASE_URL = "https://podscan.fm/api/v1"

SUMMARIZATION_PROMPT = """You are summarizing a podcast transcript for an investor and entrepreneur. You are masterful at identifying signal in the noise, and identifying insights that might help operate better, investment themes to consider, and/or specific companies or people that were mentioned that are great for whatever reason to invest into or pay attention too because they are thriving, or even better have the potential to thrive in the future. Furthermore, the goal is to identify and highlight non-obvious insights with the backup that's provided by the speakers. Many people share detailed names and insights in podcasts that they don't otherwise. Whenever you make a point, substantiate it with a quote and mention who said it.

# Notes

1. If the overall language is Chinese, make sure summary and quotes are translated to english. Don't show the Chinese.
2. Whenever you are quoting, please insert timestamp after quote in plain text format like [HH:MM:SS] - do NOT wrap it in a markdown link, just use square brackets with the time. You should take the timestamp from the beginning of the context for the quote.
3. **IMPORTANT**: Format individual insights within each section as H3 headings (###). For example: `### The Strategic Pause: Fleet Fungibility Over Rapid Expansion` followed by the description paragraph. Do NOT use bold text (**text**) for insight titles.

## Format

### 1. Key Themes (3-10 themes)
- Highlight the theme, and then below it, share the substantiation of that
- There should only be about 3-10 themes per podcast, more likely closer to 3

### 2. Contrarian Perspectives (3-5 perspectives)
- Act like Peter Thiel, and listen for things that most people would disagree with
- There should only be about 3-5 of these
- Make sure to include their facts, or experience that help substantiate the point

### 3. Companies Identified (all excellent companies)
- Companies that are mentioned for their excellence
- Format : Company Name, Description of Company, Why mentioned, Quotes

### 4. People Identified (all excellent people)
- People that are mentioned specifically for their excellence
- Format : Person Name, Description of Person, Why mentioned, Quotes

### 5. Operating Insights (1-5 insights)
- Act as Keith Rabois listening in for tactics that can be leveraged to operate better
- These should not duplicate anything in other sections

### 6. Overlooked Insights (1-2 insights)
- Act as a detective and identify the insights that were very very briefly mentioned but are actually hugely significant. Maybe the other podcast participants didn't notice, but you do.
- These should not duplicate anything in other sections"""


def sanitize_title(title: str) -> str:
    """Sanitize episode title for use as a folder name."""
    return re.sub(r'[<>:"/\\|?*]', '_', title)[:200]


# ---------------------------------------------------------------------------
# Podscan API client
# ---------------------------------------------------------------------------

def podscan_get(endpoint: str, params: dict | None = None) -> dict:
    """Authenticated GET to Podscan API with 429/403 retry."""
    url = f"{PODSCAN_BASE_URL}{endpoint}"
    headers = {"Authorization": f"Bearer {PODSCAN_API_KEY}"}

    for attempt in range(6):
        resp = requests.get(url, headers=headers, params=params, timeout=60)
        if resp.status_code == 429:
            wait = 15 * (attempt + 1)
            print(f"  Rate limited (429), waiting {wait}s...")
            time.sleep(wait)
            continue
        if resp.status_code == 403:
            try:
                data = resp.json()
                if "daily_limit" in data.get("error", ""):
                    raise RuntimeError(f"Daily API limit exceeded. Resets in {data.get('retry_after', '?')}s")
            except ValueError:
                pass
            resp.raise_for_status()
        resp.raise_for_status()
        time.sleep(2)  # Courtesy delay between requests
        return resp.json()

    raise RuntimeError(f"Podscan API rate limited after 6 retries: {endpoint}")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def fetch_podcast_config() -> dict:
    """Fetch podcast_config.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/podcast_config.json"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_podscan_status() -> dict:
    """Fetch podscan_status.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/podscan_status.json"
    resp = requests.get(url, timeout=30)
    if resp.status_code == 404:
        return {"podcasts": {}}
    resp.raise_for_status()
    return resp.json()


def find_new_episodes(config: dict, status: dict) -> list[dict]:
    """Poll Podscan for unprocessed episodes from the last N days."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    new_episodes = []

    for podcast_name, podcast_info in config.items():
        podscan_id = podcast_info.get("podscan_id")
        if not podscan_id:
            continue

        print(f"Checking {podcast_name} (podscan_id={podscan_id})...")

        try:
            status_episodes = status.get("podcasts", {}).get(podscan_id, {}).get("episodes", {})

            # Paginate through episodes until we find ones older than cutoff
            page = 1
            found_old = False
            while not found_old and page <= 3:
                data = podscan_get(f"/podcasts/{podscan_id}/episodes", {
                    "per_page": "20",
                    "page": str(page),
                })

                episodes = data.get("episodes", [])
                if not episodes:
                    break

                for ep in episodes:
                    ep_id = ep.get("episode_id", "")
                    posted_at = ep.get("posted_at", "")

                    # Check if older than cutoff
                    if posted_at:
                        try:
                            ep_date = datetime.fromisoformat(posted_at.replace("Z", "+00:00"))
                            if ep_date < cutoff:
                                found_old = True
                                continue
                        except (ValueError, TypeError):
                            pass

                    # Skip already processed
                    if ep_id in status_episodes and status_episodes[ep_id].get("status") == "summarized":
                        continue

                    new_episodes.append({
                        "podscan_episode_id": ep_id,
                        "podscan_podcast_id": podscan_id,
                        "podcast_name": podcast_name,
                        "title": ep.get("episode_title", "Unknown"),
                        "episode_url": ep.get("episode_url", ""),
                        "posted_at": posted_at,
                        "metadata": ep.get("metadata", {}),
                    })

                meta = data.get("meta", {})
                if page >= meta.get("last_page", 1):
                    break
                page += 1

        except Exception as e:
            print(f"  Error fetching episodes for {podcast_name}: {e}")
            continue

    print(f"Found {len(new_episodes)} new episode(s) to process")
    return new_episodes


# ---------------------------------------------------------------------------
# Transcript conversion
# ---------------------------------------------------------------------------

def convert_podscan_transcript(raw_transcript: str, speaker_map: dict) -> str:
    """
    Convert Podscan transcript format to our standard format with real speaker names.

    Input format: [00:00:00.000 --> 00:00:28.960] [SPEAKER_01] text
    Output format: [00:00:00] Harry Stebbings: text
    """
    lines = raw_transcript.strip().split("\n")
    converted = []

    # Pattern: [timestamp --> timestamp] [SPEAKER_XX] text
    pattern = re.compile(
        r"\[(\d{2}:\d{2}:\d{2})(?:\.\d+)?\s*-->\s*\d{2}:\d{2}:\d{2}(?:\.\d+)?\]\s*"
        r"\[?(SPEAKER_\d+)\]?\s*(.*)"
    )

    for line in lines:
        line = line.strip()
        if not line:
            continue

        m = pattern.match(line)
        if m:
            timestamp = m.group(1)
            speaker_label = m.group(2)
            text = m.group(3).strip()

            speaker_name = speaker_map.get(speaker_label, speaker_label)
            converted.append(f"[{timestamp}] {speaker_name}: {text}")
        else:
            # Pass through lines that don't match (e.g. plain text segments)
            converted.append(line)

    return "\n\n".join(converted)


def build_speaker_map(metadata: dict) -> dict:
    """
    Build SPEAKER_XX -> real name mapping from Podscan metadata.

    Podscan metadata has:
      hosts: [{ host_name, host_company?, speaker_label? }]
      guests: [{ guest_name, guest_company?, guest_occupation?, speaker_label? }]
    Or sometimes:
      speakers: { "SPEAKER_00": "Name", ... }
    """
    speaker_map = {}

    # Direct speakers map (if present)
    if "speakers" in metadata and isinstance(metadata["speakers"], dict):
        speaker_map.update(metadata["speakers"])

    # From hosts
    for host in metadata.get("hosts", []):
        if isinstance(host, dict):
            label = host.get("speaker_label", "")
            name = host.get("host_name", "")
            if label and name:
                speaker_map[label] = name

    # From guests
    for guest in metadata.get("guests", []):
        if isinstance(guest, dict):
            label = guest.get("speaker_label", "")
            name = guest.get("guest_name", "")
            if label and name:
                speaker_map[label] = name

    return speaker_map


def extract_names_from_metadata(metadata: dict) -> set[str]:
    """Extract all real speaker names from Podscan metadata."""
    names = set()

    for host in metadata.get("hosts", []):
        if isinstance(host, dict) and host.get("host_name"):
            names.add(host["host_name"])

    for guest in metadata.get("guests", []):
        if isinstance(guest, dict) and guest.get("guest_name"):
            names.add(guest["guest_name"])

    for name in metadata.get("speakers", {}).values():
        if name and not name.startswith("SPEAKER_"):
            names.add(name)

    return names


def extract_participants(metadata: dict, podcast_name: str, config: dict) -> str:
    """Extract participant names from metadata, falling back to config hosts."""
    names = extract_names_from_metadata(metadata)

    if not names:
        hosts = config.get(podcast_name, {}).get("hosts", [])
        names.update(hosts)

    names.discard("")
    return ", ".join(sorted(names))


# ---------------------------------------------------------------------------
# Summarization
# ---------------------------------------------------------------------------

def summarize_transcript(
    transcript: str,
    episode_title: str,
    podcast_name: str,
    episode_url: str,
    posted_at: str,
    participants: str,
    anthropic_api_key: str,
) -> str:
    """Summarize transcript using Claude Sonnet and format with metadata header."""
    print("  Summarizing with Claude Sonnet...")

    client = Anthropic(api_key=anthropic_api_key)

    prompt = f"""{SUMMARIZATION_PROMPT}

Episode: {episode_title}
Podcast: {podcast_name}
Participants: {participants}

Transcript:
{transcript[:100000]}"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt}],
    )

    summary_content = response.content[0].text

    # Format date
    date_formatted = format_date(posted_at)

    header = f"""# [{episode_title}]({episode_url})

**Podcast:** {podcast_name}
**Date:** {date_formatted}
**Participants:** {participants}
**Episode URL:** {episode_url}
**Transcript:** [View Transcript](./transcript.md)

---

"""

    result = header + summary_content
    print(f"  Summary generated ({len(summary_content)} chars)")
    return result


def format_date(date_str: str) -> str:
    """Format ISO date string or YYYYMMDD to readable date."""
    if not date_str:
        return "Unknown"
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        pass
    if len(date_str) == 8 and date_str.isdigit():
        return datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d")
    return date_str


# ---------------------------------------------------------------------------
# Git operations
# ---------------------------------------------------------------------------

def clone_repo(work_dir: Path) -> Repo:
    """Clone the repository."""
    repo_path = work_dir / "repo"
    auth_url = f"https://{GITHUB_TOKEN}@github.com/altmbr/Podcast_Summarizer.git"
    print("Cloning repository...")
    repo = Repo.clone_from(auth_url, repo_path)
    # Configure git user for commits
    repo.config_writer().set_value("user", "name", "Podscan Processor").release()
    repo.config_writer().set_value("user", "email", "podscan@teahose.com").release()
    print("  Repository cloned")
    return repo


def write_episode_files(
    repo: Repo,
    podcast_name: str,
    episode_title: str,
    transcript: str,
    summary: str,
) -> str:
    """Write transcript and summary files to the repo. Returns the episode directory name."""
    sanitized_title = sanitize_title(episode_title)
    episode_dir = Path(repo.working_dir) / "podcast_work" / podcast_name / sanitized_title
    episode_dir.mkdir(parents=True, exist_ok=True)

    (episode_dir / "transcript.md").write_text(transcript, encoding="utf-8")
    (episode_dir / "summary.md").write_text(summary, encoding="utf-8")

    print(f"  Wrote files to {episode_dir.relative_to(repo.working_dir)}")
    return sanitized_title


def update_podscan_status(
    repo: Repo,
    status: dict,
    podscan_podcast_id: str,
    podcast_name: str,
    episode_id: str,
    episode_title: str,
    posted_at: str,
) -> dict:
    """Update podscan_status.json in the repo."""
    if podscan_podcast_id not in status.get("podcasts", {}):
        status.setdefault("podcasts", {})[podscan_podcast_id] = {
            "podcast_name": podcast_name,
            "episodes": {},
        }

    status["podcasts"][podscan_podcast_id]["episodes"][episode_id] = {
        "title": episode_title,
        "status": "summarized",
        "posted_at": posted_at,
        "processed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    status_path = Path(repo.working_dir) / "podscan_status.json"
    status_path.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")

    return status


def commit_and_push(repo: Repo, processed_episodes: list[dict]):
    """Commit all changes and push."""
    repo.git.add(A=True)

    # Check if there are staged changes
    if not repo.index.diff("HEAD") and not repo.untracked_files:
        print("No changes to commit")
        return

    titles = [ep["title"] for ep in processed_episodes]
    commit_msg = f"Add {len(titles)} new podcast episode(s)\n\n"
    commit_msg += "\n".join(f"- {t}" for t in titles)
    commit_msg += "\n\n🤖 Generated with Podscan Processor"

    repo.index.commit(commit_msg)
    print("  Changes committed")

    origin = repo.remote("origin")
    origin.push()
    print("  Pushed to GitHub")


# ---------------------------------------------------------------------------
# Notification
# ---------------------------------------------------------------------------

def send_processing_report(processed: list[dict], failed: list[dict]):
    """Send processing report via SendGrid."""
    if not SENDGRID_API_KEY:
        print("No SENDGRID_API_KEY, skipping email report")
        return

    total = len(processed) + len(failed)
    if total == 0:
        return

    html = ["<html><body>"]
    html.append("<h2>Podscan Processor Report</h2>")
    html.append(f"<p>Processed {len(processed)}/{total} episodes</p>")

    if processed:
        html.append("<h3>Processed:</h3><ul>")
        for ep in processed:
            html.append(f"<li><strong>[{ep['podcast_name']}]</strong> {ep['title']}</li>")
        html.append("</ul>")

    if failed:
        html.append("<h3>Failed:</h3><ul>")
        for ep in failed:
            html.append(
                f"<li><strong>[{ep['podcast_name']}]</strong> {ep['title']}"
                f"<br/><small>{ep.get('error', 'Unknown error')}</small></li>"
            )
        html.append("</ul>")

    html.append("</body></html>")

    subject = f"Podscan: {len(processed)} processed"
    if failed:
        subject += f", {len(failed)} failed"

    requests.post(
        "https://api.sendgrid.com/v3/mail/send",
        headers={
            "Authorization": f"Bearer {SENDGRID_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "personalizations": [{"to": [{"email": NOTIFICATION_EMAIL}]}],
            "from": {"email": "podscan@teahose.com", "name": "Podscan Processor"},
            "subject": subject,
            "content": [{"type": "text/html", "value": "\n".join(html)}],
        },
    )


# ---------------------------------------------------------------------------
# Episode processing
# ---------------------------------------------------------------------------

def check_already_processed(repo: Repo, podcast_name: str, episode_title: str) -> bool:
    """Check if summary.md already exists for this episode."""
    summary_path = Path(repo.working_dir) / "podcast_work" / podcast_name / sanitize_title(episode_title) / "summary.md"
    return summary_path.exists()


def process_episode(episode: dict, config: dict, repo: Repo, status: dict) -> bool:
    """Process a single episode: fetch transcript from Podscan, summarize, write files."""
    ep_id = episode["podscan_episode_id"]
    title = episode["title"]
    podcast_name = episode["podcast_name"]
    episode_url = episode["episode_url"]
    posted_at = episode["posted_at"]
    podscan_podcast_id = episode["podscan_podcast_id"]

    print(f"\n{'='*60}")
    print(f"Processing: {title}")
    print(f"Podcast: {podcast_name}")
    print(f"{'='*60}")

    # Check if already processed on disk
    if check_already_processed(repo, podcast_name, title):
        print(f"  Already processed (summary.md exists), skipping")
        update_podscan_status(repo, status, podscan_podcast_id, podcast_name, ep_id, title, posted_at)
        return True

    # Step 1: Fetch transcript from Podscan
    print("  Step 1/2: Fetching transcript from Podscan...")
    ep_data = podscan_get(f"/episodes/{ep_id}")
    raw_transcript = ep_data.get("episode_transcript", "")
    if not raw_transcript:
        raise ValueError(f"No transcript available for episode {ep_id}")

    metadata = ep_data.get("metadata", episode.get("metadata", {}))
    speaker_map = build_speaker_map(metadata)

    # Convert transcript with real speaker names
    transcript = convert_podscan_transcript(raw_transcript, speaker_map)
    participants = extract_participants(metadata, podcast_name, config)

    print(f"  Transcript: {len(transcript)} chars, {len(speaker_map)} speakers identified")

    # Step 2: Summarize with Claude
    print("  Step 2/2: Summarizing...")
    summary = summarize_transcript(
        transcript, title, podcast_name,
        episode_url, posted_at, participants,
        ANTHROPIC_API_KEY,
    )

    # Write files
    write_episode_files(repo, podcast_name, title, transcript, summary)

    # Update status
    update_podscan_status(repo, status, podscan_podcast_id, podcast_name, ep_id, title, posted_at)

    print(f"  Done: {title}")
    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

@functions_framework.http
def podscan_processor(request):
    """HTTP entry point triggered by Cloud Scheduler."""
    print("Podscan processor triggered")

    # Allow dry-run via query param
    dry_run = False
    if request:
        dry_run = request.args.get("dry_run", "false").lower() == "true"

    if not PODSCAN_API_KEY:
        return {"status": "error", "message": "PODSCAN_API_KEY not set"}, 500
    if not ANTHROPIC_API_KEY:
        return {"status": "error", "message": "ANTHROPIC_API_KEY not set"}, 500
    if not GITHUB_TOKEN and not dry_run:
        return {"status": "error", "message": "GITHUB_TOKEN not set"}, 500

    try:
        # Fetch config and status
        config = fetch_podcast_config()
        status = fetch_podscan_status()

        # Find new episodes
        new_episodes = find_new_episodes(config, status)
        if not new_episodes:
            print("No new episodes found")
            return {"status": "ok", "message": "No new episodes", "count": 0}

        # Clone repo
        with tempfile.TemporaryDirectory() as work_dir:
            work_path = Path(work_dir)

            if not dry_run:
                repo = clone_repo(work_path)
            else:
                # For dry run, create a local repo
                repo_path = work_path / "repo"
                repo_path.mkdir(parents=True)
                repo = Repo.init(repo_path)
                (repo_path / "podcast_work").mkdir()

            # Process each episode
            processed = []
            failed = []

            for episode in new_episodes:
                try:
                    success = process_episode(episode, config, repo, status)
                    if success:
                        processed.append(episode)
                except Exception as e:
                    print(f"  Error: {e}")
                    traceback.print_exc()
                    episode["error"] = str(e)
                    failed.append(episode)

            # Commit and push
            if processed and not dry_run:
                commit_and_push(repo, processed)

            # Send report
            send_processing_report(processed, failed)

            result = {
                "status": "ok",
                "processed": len(processed),
                "failed": len(failed),
                "dry_run": dry_run,
                "episodes": [
                    {"title": ep["title"], "podcast": ep["podcast_name"]}
                    for ep in processed
                ],
            }

            if failed:
                result["errors"] = [
                    {"title": ep["title"], "error": ep.get("error", "Unknown")}
                    for ep in failed
                ]

            print(f"\nDone: {len(processed)} processed, {len(failed)} failed")
            return result

    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
        return {"status": "error", "message": str(e)}, 500
