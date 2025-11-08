#!/usr/bin/env python3
"""
Clean up incomplete podcast episodes:
- Delete episode folders without summary.md
- Reset their status to "discovered" in podcast_status.json
"""

import os
import json
import shutil
import sys
from pathlib import Path

PODCAST_WORK_DIR = Path("./podcast_work")
PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_STATUS_MD_FILE = Path("./podcast_status.md")

def load_podcast_status():
    """Load podcast episode status tracking"""
    if PODCAST_STATUS_FILE.exists():
        with open(PODCAST_STATUS_FILE, 'r') as f:
            return json.load(f)
    return {"podcasts": {}}

def save_podcast_status(status_data):
    """Save podcast status to file"""
    with open(PODCAST_STATUS_FILE, 'w') as f:
        json.dump(status_data, f, indent=2)

def generate_status_markdown(status_data):
    """Generate a human-readable markdown file from status data"""
    lines = ["# Podcast Status Tracking\n\n"]

    podcasts = status_data.get("podcasts", {})

    for url, podcast_data in podcasts.items():
        podcast_name = podcast_data.get("podcast_name", "Unknown")
        lines.append(f"## {podcast_name}\n\n")

        episodes = podcast_data.get("episodes", {})
        lines.append(f"**Total Episodes:** {len(episodes)}\n\n")

        # Count by status
        status_counts = {}
        for ep_data in episodes.values():
            status = ep_data.get("status", "unknown")
            status_counts[status] = status_counts.get(status, 0) + 1

        lines.append("**Status Summary:**\n")
        for status, count in sorted(status_counts.items()):
            lines.append(f"- {status}: {count}\n")

        lines.append("\n**Episodes:**\n\n")

        for vid_id, episode in episodes.items():
            title = episode.get("title", "Unknown")[:80]
            status = episode.get("status", "unknown")
            upload_date = episode.get("upload_date", "N/A")
            discovered = episode.get("discovered_date", "N/A")

            # Format upload_date from YYYYMMDD to YYYY-MM-DD
            if upload_date and upload_date != "N/A" and len(upload_date) == 8:
                try:
                    upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
                except:
                    pass

            status_emoji = {
                "discovered": "🔍",
                "downloaded": "⬇️",
                "transcribed": "📝",
                "summarized": "✅"
            }.get(status, "❓")

            lines.append(f"- {status_emoji} **{title}**\n")
            lines.append(f"  - ID: `{vid_id}`\n")
            lines.append(f"  - Published: {upload_date}\n")
            lines.append(f"  - Status: `{status}`\n")
            lines.append(f"  - Discovered: {discovered}\n\n")

        lines.append("---\n\n")

    with open(PODCAST_STATUS_MD_FILE, 'w') as f:
        f.writelines(lines)

def find_episode_in_status(status_data, podcast_name, episode_folder_name):
    """Try to find an episode in status by matching folder name to episode title"""
    for url, podcast_data in status_data.get("podcasts", {}).items():
        if podcast_data.get("podcast_name") == podcast_name:
            for vid_id, episode in podcast_data.get("episodes", {}).items():
                # Sanitize the episode title to match folder name
                import re
                sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', episode.get("title", ""))
                sanitized_title = sanitized_title.strip('. ')

                if sanitized_title == episode_folder_name:
                    return url, vid_id
    return None, None

def main():
    print("🧹 Starting cleanup of incomplete episodes...\n")

    # Load status
    status_data = load_podcast_status()

    # Track what we're doing
    episodes_to_delete = []
    episodes_deleted = 0
    episodes_status_reset = 0

    # Scan podcast_work directory
    if not PODCAST_WORK_DIR.exists():
        print(f"❌ {PODCAST_WORK_DIR} does not exist")
        return

    # Iterate through podcast folders
    for podcast_folder in PODCAST_WORK_DIR.iterdir():
        if not podcast_folder.is_dir():
            continue

        podcast_name = podcast_folder.name
        print(f"📁 Checking podcast: {podcast_name}")

        # Iterate through episode folders
        for episode_folder in podcast_folder.iterdir():
            if not episode_folder.is_dir():
                continue

            episode_name = episode_folder.name
            summary_file = episode_folder / "summary.md"

            # Check if summary.md exists
            if not summary_file.exists():
                episodes_to_delete.append({
                    'podcast_name': podcast_name,
                    'episode_name': episode_name,
                    'path': episode_folder
                })

    if not episodes_to_delete:
        print("\n✓ No incomplete episodes found. All episodes have summaries!")
        return

    # Show what will be deleted
    print(f"\n{'='*70}")
    print(f"Found {len(episodes_to_delete)} incomplete episode(s) to delete:")
    print(f"{'='*70}\n")

    for ep in episodes_to_delete:
        print(f"  - [{ep['podcast_name']}] {ep['episode_name']}")

    print(f"\n{'='*70}")

    # Check if --confirm flag is present
    if "--confirm" not in sys.argv:
        print("To proceed with deletion, run: python3 cleanup_incomplete.py --confirm")
        return

    print("Proceeding with deletion (--confirm flag detected)...")

    # Delete folders and update status
    print("\n🗑️  Deleting incomplete episodes...\n")

    for ep in episodes_to_delete:
        # Delete the folder
        try:
            shutil.rmtree(ep['path'])
            print(f"  ✓ Deleted: {ep['podcast_name']}/{ep['episode_name']}")
            episodes_deleted += 1

            # Find and update status
            podcast_url, video_id = find_episode_in_status(
                status_data,
                ep['podcast_name'],
                ep['episode_name']
            )

            if podcast_url and video_id:
                # Reset status to "discovered"
                status_data["podcasts"][podcast_url]["episodes"][video_id]["status"] = "discovered"
                status_data["podcasts"][podcast_url]["episodes"][video_id]["discovered_date"] = None
                print(f"    ↳ Reset status to 'discovered' for video ID: {video_id}")
                episodes_status_reset += 1
            else:
                print(f"    ⚠ Could not find episode in status file")

        except Exception as e:
            print(f"  ❌ Error deleting {ep['path']}: {e}")

    # Save updated status
    save_podcast_status(status_data)
    generate_status_markdown(status_data)

    print(f"\n{'='*70}")
    print(f"✓ Cleanup complete!")
    print(f"  - Episodes deleted: {episodes_deleted}")
    print(f"  - Statuses reset: {episodes_status_reset}")
    print(f"  - Status files updated")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
