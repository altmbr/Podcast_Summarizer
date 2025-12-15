"""Update podcast status file."""
import json
from pathlib import Path
from datetime import datetime


def update_podcast_status(
    status_file: Path,
    podcast_url: str,
    video_id: str,
    status: str
):
    """
    Update episode status in podcast_status.json.

    Args:
        status_file: Path to podcast_status.json
        podcast_url: Podcast playlist URL
        video_id: Episode video ID
        status: New status (e.g., "summarized")
    """
    print(f"Updating status for {video_id} to '{status}'...")

    # Load current status
    with open(status_file, 'r') as f:
        data = json.load(f)

    # Update episode status
    if podcast_url in data.get("podcasts", {}):
        if video_id in data["podcasts"][podcast_url].get("episodes", {}):
            data["podcasts"][podcast_url]["episodes"][video_id]["status"] = status
            data["podcasts"][podcast_url]["episodes"][video_id]["discovered_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save updated status
    with open(status_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"✓ Status updated")
