#!/usr/bin/env python3
"""Backfill upload_date for existing episodes from YouTube metadata"""
import json
import subprocess
import sys
from pathlib import Path

status_file = Path("./podcast_status.json")

if not status_file.exists():
    print(f"❌ Error: {status_file} not found")
    exit(1)

with open(status_file, 'r') as f:
    data = json.load(f)

total_filled = 0
total_skipped = 0
total_errors = 0
total_processed = 0

print("🔄 Backfilling upload dates from YouTube...")
print("(This may take a while for large libraries)")
print()

for url, podcast_data in data.get('podcasts', {}).items():
    podcast_name = podcast_data.get('podcast_name', 'Unknown')
    print(f"📻 {podcast_name}")
    sys.stdout.flush()

    episodes = podcast_data.get('episodes', {})
    for vid_id, episode in episodes.items():
        total_processed += 1

        # Show progress every 50 episodes
        if total_processed % 50 == 0:
            print(f"  [Progress: {total_processed}/{sum(len(p.get('episodes', {})) for p in data.get('podcasts', {}).values())}]")
            sys.stdout.flush()

        if not episode.get('upload_date'):
            title = episode.get('title', 'Unknown')[:50]

            # Skip private videos
            if '[Private video]' in title:
                total_skipped += 1
                continue

            try:
                video_url = f"https://www.youtube.com/watch?v={vid_id}"
                cmd = ["yt-dlp", "-j", "--no-warnings", "--socket-timeout", "5", video_url]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=8)

                if result.returncode == 0:
                    try:
                        metadata = json.loads(result.stdout)
                        upload_date = metadata.get('upload_date')
                        if upload_date:
                            episode['upload_date'] = upload_date
                            total_filled += 1
                            if total_filled % 10 == 0:
                                print(f"  ✓ Processed {total_filled} episodes with dates")
                            sys.stdout.flush()
                        else:
                            total_errors += 1
                    except json.JSONDecodeError:
                        total_errors += 1
                else:
                    total_errors += 1
            except subprocess.TimeoutExpired:
                total_errors += 1
            except Exception as e:
                total_errors += 1
        else:
            total_skipped += 1

    print()
    sys.stdout.flush()

# Save updated data
print("Saving results...")
sys.stdout.flush()

with open(status_file, 'w') as f:
    json.dump(data, f, indent=2)

# Regenerate markdown
from podcast_summarizer import generate_status_markdown
generate_status_markdown(data)

print()
print("✓ Backfill complete!")
print(f"  - Filled with dates: {total_filled}")
print(f"  - Already had dates: {total_skipped}")
print(f"  - Errors/timeouts: {total_errors}")
print(f"  - Total processed: {total_processed}")
print(f"  - Status file updated: {status_file}")
print(f"  - Markdown regenerated: podcast_status.md")
