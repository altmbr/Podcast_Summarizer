#!/usr/bin/env python3
"""
Quick script to check which episodes would be included in the weekly summary
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

PODCAST_STATUS_FILE = Path("./podcast_status.json")

# Load status
with open(PODCAST_STATUS_FILE, 'r') as f:
    status_data = json.load(f)

# Calculate cutoff (same logic as generate_weekly_summary.py)
cutoff_date = (datetime.now() - timedelta(days=8)).replace(hour=0, minute=0, second=0, microsecond=0)

print(f"Cutoff date: {cutoff_date.strftime('%Y-%m-%d')}")
print(f"Looking for episodes published on or after: {cutoff_date.strftime('%Y-%m-%d')}\n")

episodes = []

for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
    podcast_name = podcast_data.get("podcast_name", "Unknown")

    if not podcast_name or podcast_name == "None":
        continue

    for video_id, episode_data in podcast_data.get("episodes", {}).items():
        # Only include summarized episodes
        if episode_data.get("status") != "summarized":
            continue

        # Check upload_date
        upload_date = episode_data.get("upload_date")
        if not upload_date or len(upload_date) != 8:
            continue

        try:
            episode_date = datetime.strptime(upload_date, '%Y%m%d')
            if episode_date >= cutoff_date:
                episodes.append({
                    "podcast_name": podcast_name,
                    "title": episode_data.get("title", "Unknown"),
                    "upload_date": upload_date,
                    "upload_date_formatted": f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}",
                    "episode_date": episode_date
                })
        except ValueError:
            continue

# Sort by date (newest first)
episodes.sort(key=lambda x: x["episode_date"], reverse=True)

print(f"Found {len(episodes)} episodes:\n")

for i, ep in enumerate(episodes, 1):
    print(f"{i}. [{ep['podcast_name']}] {ep['title']}")
    print(f"   Published: {ep['upload_date_formatted']}\n")
