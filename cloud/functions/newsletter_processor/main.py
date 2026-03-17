"""
Newsletter Processor Cloud Function
Receives email newsletters via webhook from Cloudflare Email Worker,
summarizes with Claude, and pushes to git for publishing on teahose.com.
"""

import functions_framework
import hashlib
import hmac
import json
import os
import re
import subprocess
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path

import html2text
import requests
from anthropic import Anthropic
from bs4 import BeautifulSoup
from git import Repo


# Configuration
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
WEBHOOK_SECRET = os.environ.get("NEWSLETTER_WEBHOOK_SECRET")
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", "altmbr@gmail.com")
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/altmbr/Podcast_Summarizer/main"

GCS_BACKUP_BUCKET = "gen-lang-client-0111593271-podscan-backups"

NEWSLETTER_SUMMARIZATION_PROMPT = """You are summarizing a newsletter article for an investor and entrepreneur. Identify the highest-signal insights: investment themes, operating tactics, market shifts, companies to watch, and contrarian takes. Whenever you make a point, substantiate it with a direct quote from the article.

## Format

### 1. Key Themes (2-5 themes)
- Highlight the theme, and then below it, share the substantiation
- Format individual insights within each section as H3 headings (###)

### 2. Contrarian Perspectives (1-3 perspectives)
- Non-obvious or against-consensus views with supporting reasoning
- Make sure to include their facts or evidence that help substantiate the point

### 3. Companies Identified (all notable companies)
- Companies mentioned for their excellence or as case studies
- Format: Company Name, Description, Why mentioned, Quotes

### 4. People Identified (all notable people)
- People mentioned for specific expertise or achievement
- Format: Person Name, Description, Why mentioned, Quotes

### 5. Operating Insights (1-3 insights)
- Tactical takeaways for operators and entrepreneurs

### 6. Overlooked Insights (1-2 insights)
- Briefly mentioned but potentially significant details
- These should not duplicate anything in other sections"""


def sanitize_title(title: str) -> str:
    """Sanitize title for use as a folder name."""
    return re.sub(r'[<>:"/\\|?*]', '_', title)[:200]


# ---------------------------------------------------------------------------
# Webhook authentication
# ---------------------------------------------------------------------------

def verify_webhook_signature(request) -> bool:
    """Verify HMAC-SHA256 signature from Cloudflare Email Worker."""
    if not WEBHOOK_SECRET:
        print("WARNING: NEWSLETTER_WEBHOOK_SECRET not set, skipping auth")
        return True

    signature = request.headers.get("X-Webhook-Signature", "")
    body = request.get_data(as_text=True)
    expected = hmac.new(WEBHOOK_SECRET.encode(), body.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, expected)


# ---------------------------------------------------------------------------
# Content extraction
# ---------------------------------------------------------------------------

def extract_newsletter_content(html_body: str, text_body: str) -> str:
    """Extract article content from newsletter HTML, falling back to plain text."""
    if html_body:
        soup = BeautifulSoup(html_body, "html.parser")

        # Remove noise elements
        for tag in soup.find_all(["style", "script", "noscript"]):
            tag.decompose()

        # Remove tracking pixels (collect first, then decompose to avoid mutation during iteration)
        to_remove = []
        for img in soup.find_all("img"):
            try:
                src = (img.get("src") or "").lower()
                width = img.get("width") or ""
                height = img.get("height") or ""
                if width in ("1", "0") or height in ("1", "0") or "track" in src or "pixel" in src:
                    to_remove.append(img)
            except Exception:
                continue
        for img in to_remove:
            img.decompose()

        # Convert to readable text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = True
        h.body_width = 0  # No line wrapping
        content = h.handle(str(soup))

        if len(content.strip()) > 200:
            return content.strip()

    # Fallback to plain text
    if text_body and len(text_body.strip()) > 200:
        return text_body.strip()

    return ""


# ---------------------------------------------------------------------------
# Newsletter config
# ---------------------------------------------------------------------------

def fetch_newsletter_config() -> dict:
    """Fetch newsletter_config.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/newsletter_config.json"
    resp = requests.get(url, timeout=15)
    if resp.status_code == 200:
        return resp.json()
    print(f"newsletter_config.json not found ({resp.status_code}), using empty config")
    return {}


def resolve_newsletter_name(from_address: str, from_name: str, config: dict) -> tuple[str, str]:
    """Resolve sender to newsletter name and author. Returns (newsletter_name, author_name)."""
    # Check config for known senders
    sender_config = config.get(from_address.lower(), {})
    if sender_config:
        return sender_config.get("name", from_name), sender_config.get("author", from_name)

    # Check domain-level config
    domain = from_address.split("@")[-1] if "@" in from_address else ""
    domain_config = config.get(domain, {})
    if domain_config:
        return domain_config.get("name", from_name), domain_config.get("author", from_name)

    # Fallback: use sender name or email domain
    if from_name:
        return from_name, from_name
    return domain.split(".")[0].title() if domain else "Unknown Newsletter", from_address


# ---------------------------------------------------------------------------
# Status tracking
# ---------------------------------------------------------------------------

def fetch_newsletter_status() -> dict:
    """Fetch newsletter_status.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/newsletter_status.json"
    resp = requests.get(url, timeout=15)
    if resp.status_code == 200:
        return resp.json()
    return {"newsletters": {}}


def make_episode_key(from_address: str, subject: str, date: str) -> str:
    """Create a dedup key from sender + subject + date."""
    raw = f"{from_address}|{subject}|{date}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def is_already_processed(status: dict, newsletter_name: str, episode_key: str) -> bool:
    """Check if this newsletter has already been processed."""
    episodes = status.get("newsletters", {}).get(newsletter_name, {}).get("episodes", {})
    return episode_key in episodes and episodes[episode_key].get("status") == "summarized"


def update_newsletter_status(repo: Repo, status: dict, newsletter_name: str, episode_key: str, subject: str):
    """Update newsletter_status.json in the repo."""
    if newsletter_name not in status.get("newsletters", {}):
        status.setdefault("newsletters", {})[newsletter_name] = {"episodes": {}}

    status["newsletters"][newsletter_name]["episodes"][episode_key] = {
        "subject": subject,
        "status": "summarized",
        "processed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    status_path = Path(repo.working_dir) / "newsletter_status.json"
    status_path.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Git operations (mirrored from podscan_processor)
# ---------------------------------------------------------------------------

def verify_github_auth():
    """Verify GitHub token has push access."""
    print("Verifying GitHub auth...")
    result = subprocess.run(
        ["git", "ls-remote", f"https://{GITHUB_TOKEN}@github.com/altmbr/Podcast_Summarizer.git", "HEAD"],
        capture_output=True, text=True, timeout=15,
    )
    if result.returncode != 0:
        raise RuntimeError(f"GitHub auth failed: {result.stderr.strip()}")
    print("  GitHub auth verified")


def clone_repo(work_dir: Path) -> Repo:
    """Clone the repository."""
    repo_path = work_dir / "repo"
    auth_url = f"https://{GITHUB_TOKEN}@github.com/altmbr/Podcast_Summarizer.git"
    print("Cloning repository...")
    repo = Repo.clone_from(auth_url, repo_path)
    repo.config_writer().set_value("user", "name", "Newsletter Processor").release()
    repo.config_writer().set_value("user", "email", "newsletter@teahose.com").release()
    print("  Repository cloned")
    return repo


def backup_to_gcs(repo: Repo):
    """Save a git bundle to GCS if push fails."""
    try:
        from google.cloud import storage
        bundle_path = Path(repo.working_dir).parent / "backup.bundle"
        repo.git.bundle("create", str(bundle_path), "--all")
        client = storage.Client()
        bucket = client.bucket(GCS_BACKUP_BUCKET)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        blob = bucket.blob(f"bundles/newsletter_{timestamp}.bundle")
        blob.upload_from_filename(str(bundle_path))
        print(f"  Backup saved to gs://{GCS_BACKUP_BUCKET}/{blob.name}")
    except Exception as e:
        print(f"  WARNING: Backup to GCS also failed: {e}")


def commit_and_push(repo: Repo, subject: str):
    """Commit and push. Backs up to GCS if push fails."""
    repo.git.add(A=True)

    if not repo.index.diff("HEAD") and not repo.untracked_files:
        print("No changes to commit")
        return

    commit_msg = f"Add newsletter summary: {subject}\n\n🤖 Generated with Newsletter Processor"
    repo.index.commit(commit_msg)
    print("  Changes committed")

    try:
        origin = repo.remote("origin")
        origin.push()
        print("  Pushed to GitHub")
    except Exception as e:
        print(f"  ERROR: Push failed: {e}")
        print("  Saving backup to GCS...")
        backup_to_gcs(repo)
        raise


# ---------------------------------------------------------------------------
# Summarization
# ---------------------------------------------------------------------------

def summarize_newsletter(
    content: str,
    subject: str,
    newsletter_name: str,
    author_name: str,
    date_str: str,
) -> str:
    """Summarize newsletter content with Claude and format with metadata header."""
    print("  Summarizing with Claude Sonnet...")

    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""{NEWSLETTER_SUMMARIZATION_PROMPT}

Newsletter: {newsletter_name}
Subject: {subject}
Author: {author_name}

Article:
{content[:100000]}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt}],
    )

    summary_content = response.content[0].text

    # Format date
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        date_formatted = dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        date_formatted = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    processed_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    header = f"""# {subject}

**Podcast:** {newsletter_name}
**Date:** {date_formatted}
**Processed:** {processed_at}
**Participants:** {author_name}
**Source:** newsletter

---

"""

    result = header + summary_content
    print(f"  Summary generated ({len(summary_content)} chars)")
    return result


# ---------------------------------------------------------------------------
# Notification
# ---------------------------------------------------------------------------

def send_processing_report(subject: str, newsletter_name: str, success: bool, error: str = ""):
    """Send processing report via AWS SES."""
    aws_key = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret = os.environ.get("AWS_SECRET_ACCESS_KEY")
    if not aws_key or not aws_secret:
        return

    status_text = "✓ Processed" if success else f"✗ Failed: {error}"
    html = f"<html><body><h2>Newsletter Processor</h2><p><strong>{newsletter_name}:</strong> {subject}</p><p>{status_text}</p></body></html>"

    try:
        import boto3
        ses = boto3.client("ses", region_name="us-west-2",
                           aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
        ses.send_email(
            Source="Newsletter Processor <newsletter@teahose.com>",
            Destination={"ToAddresses": [NOTIFICATION_EMAIL]},
            Message={
                "Subject": {"Data": f"Newsletter: {newsletter_name} - {'OK' if success else 'FAILED'}"},
                "Body": {"Html": {"Data": html}},
            },
        )
    except Exception as e:
        print(f"Failed to send report: {e}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

@functions_framework.http
def newsletter_processor(request):
    """HTTP entry point triggered by Cloudflare Email Worker."""
    if request.method != "POST":
        return {"error": "Method not allowed"}, 405

    if not verify_webhook_signature(request):
        return {"error": "Invalid signature"}, 401

    if not ANTHROPIC_API_KEY:
        return {"error": "ANTHROPIC_API_KEY not set"}, 500
    if not GITHUB_TOKEN:
        return {"error": "GITHUB_TOKEN not set"}, 500

    subject = "?"
    newsletter_name = "Unknown"

    try:
        payload = request.get_json()
        from_address = payload.get("from_address", "")
        from_name = payload.get("from_name", "")
        subject = payload.get("subject", "(no subject)")
        html_body = payload.get("html", "")
        text_body = payload.get("text", "")
        date_str = payload.get("date", "")

        print(f"Newsletter received: {subject}")
        print(f"  From: {from_name} <{from_address}>")

        # Resolve newsletter identity
        config = fetch_newsletter_config()
        newsletter_name, author_name = resolve_newsletter_name(from_address, from_name, config)
        print(f"  Newsletter: {newsletter_name} ({author_name})")

        # Verify GitHub auth
        verify_github_auth()

        # Check dedup
        status = fetch_newsletter_status()
        episode_key = make_episode_key(from_address, subject, date_str)

        if is_already_processed(status, newsletter_name, episode_key):
            print("  Already processed, skipping")
            return {"status": "ok", "message": "Already processed"}

        # Extract content
        content = extract_newsletter_content(html_body, text_body)
        if not content:
            return {"status": "error", "message": "No extractable content"}, 400
        print(f"  Extracted {len(content)} chars")

        # Clone repo
        with tempfile.TemporaryDirectory() as work_dir:
            work_path = Path(work_dir)
            repo = clone_repo(work_path)

            # Summarize
            summary = summarize_newsletter(content, subject, newsletter_name, author_name, date_str)

            # Write summary
            sanitized_subject = sanitize_title(subject)
            episode_dir = Path(repo.working_dir) / "podcast_work" / newsletter_name / sanitized_subject
            episode_dir.mkdir(parents=True, exist_ok=True)
            (episode_dir / "summary.md").write_text(summary, encoding="utf-8")
            print(f"  Wrote to podcast_work/{newsletter_name}/{sanitized_subject}")

            # Update status
            update_newsletter_status(repo, status, newsletter_name, episode_key, subject)

            # Commit and push
            commit_and_push(repo, subject)

        send_processing_report(subject, newsletter_name, success=True)

        return {
            "status": "ok",
            "newsletter": newsletter_name,
            "subject": subject,
        }

    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        send_processing_report(subject, newsletter_name, success=False, error=str(e))
        return {"status": "error", "message": str(e)}, 500
