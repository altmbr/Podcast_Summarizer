#!/usr/bin/env python3
"""
Standardize all summary.md files to have complete, consistent metadata.
Fills in missing fields from podcast_status.json.
"""

import re
import json
from pathlib import Path
from datetime import datetime

PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_WORK_DIR = Path("./podcast_work")

def load_podcast_status():
    """Load podcast status from JSON file"""
    with open(PODCAST_STATUS_FILE, 'r') as f:
        return json.load(f)

def convert_timestamp_to_seconds(timestamp_str):
    """Convert [HH:MM:SS] or [MM:SS] to total seconds"""
    time_str = timestamp_str.strip('[]')
    parts = time_str.split(':')

    if len(parts) == 3:  # HH:MM:SS
        h, m, s = map(int, parts)
        return h * 3600 + m * 60 + s
    elif len(parts) == 2:  # MM:SS
        m, s = map(int, parts)
        return m * 60 + s
    return 0

def create_youtube_timestamp_url(video_id, timestamp_str, offset_seconds=-10):
    """Create YouTube timestamp URL with offset (default -10 seconds)"""
    total_seconds = convert_timestamp_to_seconds(timestamp_str)
    adjusted_seconds = max(0, total_seconds + offset_seconds)

    h = adjusted_seconds // 3600
    m = (adjusted_seconds % 3600) // 60
    s = adjusted_seconds % 60

    if h > 0:
        time_param = f"{h}h{m}m{s}s"
    elif m > 0:
        time_param = f"{m}m{s}s"
    else:
        time_param = f"{s}s"

    return f"https://www.youtube.com/watch?v={video_id}&t={time_param}"

def is_xiaoyuzhou_url(url):
    """Check if URL is from Xiaoyuzhou platform"""
    return 'xiaoyuzhoufm.com' in url if url else False

def find_episode_in_status(status_data, summary_path):
    """Find episode metadata in status file by searching for folder name match"""
    episode_folder_name = summary_path.parent.name
    podcast_folder_name = summary_path.parent.parent.name

    for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
        if podcast_data.get("podcast_name") == podcast_folder_name:
            for video_id, episode_data in podcast_data.get("episodes", {}).items():
                # Try to match by folder name or title similarity
                title = episode_data.get("title", "")
                sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title).strip('. ')

                if sanitized_title == episode_folder_name or episode_folder_name in sanitized_title:
                    return {
                        "video_id": video_id,
                        "title": title,
                        "upload_date": episode_data.get("upload_date", ""),
                        "region": episode_data.get("region", "Western"),
                        "podcast_url": podcast_url
                    }
    return None

def extract_metadata_from_content(content):
    """Extract existing metadata from summary content"""
    metadata = {}

    # Extract title (first H1)
    title_match = re.search(r'^#\s+(?:\[)?([^\]\n]+)(?:\])?', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()

    # Extract fields
    for field in ['Podcast', 'Date', 'Participants', 'Region', 'Video ID', 'Video URL', 'Transcript']:
        pattern = rf'\*\*{field}:\*\*\s*(.+)'
        match = re.search(pattern, content)
        if match:
            metadata[field.lower().replace(' ', '_')] = match.group(1).strip()

    return metadata

def standardize_summary(summary_path, status_data):
    """Standardize a single summary file"""

    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract current metadata
    current_meta = extract_metadata_from_content(content)

    # Find episode in status
    episode_meta = find_episode_in_status(status_data, summary_path)

    if not episode_meta:
        print(f"  ⚠️  Could not find in status: {summary_path.parent.name}")
        return False

    # Build video URL
    video_id = episode_meta['video_id']
    if is_xiaoyuzhou_url(episode_meta.get('podcast_url', '')):
        video_url = f"https://www.xiaoyuzhoufm.com/episode/{video_id}"
    else:
        video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Format date
    upload_date = episode_meta.get('upload_date', '')
    if upload_date and len(upload_date) == 8:
        try:
            date_obj = datetime.strptime(upload_date, '%Y%m%d')
            formatted_date = date_obj.strftime('%B %d, %Y')
        except:
            formatted_date = current_meta.get('date', 'Unknown')
    else:
        formatted_date = current_meta.get('date', 'Unknown')

    # Build standardized header
    title = episode_meta['title']
    podcast_name = summary_path.parent.parent.name
    region = episode_meta.get('region', 'Western')
    participants = current_meta.get('participants', '')

    # Build new header
    is_xiaoyuzhou = is_xiaoyuzhou_url(episode_meta.get('podcast_url', ''))

    if is_xiaoyuzhou:
        new_header = f"# {title}\n\n"
    else:
        new_header = f"# [{title}]({video_url})\n\n"

    new_header += f"**Podcast:** {podcast_name}\n"
    new_header += f"**Date:** {formatted_date}\n"

    if participants:
        new_header += f"**Participants:** {participants}\n"

    new_header += f"**Region:** {region}\n"
    new_header += f"**Video ID:** {video_id}\n"
    new_header += f"**Video URL:** {video_url}\n"
    new_header += f"**Transcript:** [View Transcript](./transcript.md)\n\n"
    new_header += "---\n\n"

    # Find where summary content starts (after first ---)
    content_match = re.search(r'^---\s*$(.+)', content, re.MULTILINE | re.DOTALL)
    if content_match:
        summary_content = content_match.group(1).strip()
    else:
        # Try to find content after metadata
        content_match = re.search(r'\*\*Transcript:\*\*.+?\n\n(.+)', content, re.DOTALL)
        if content_match:
            summary_content = content_match.group(1).strip()
        else:
            summary_content = content

    # Make timestamps clickable (YouTube only)
    if not is_xiaoyuzhou:
        timestamp_pattern = r'(?<!\])\[(\d{1,2}:\d{2}:\d{2}|\d{1,2}:\d{2})\](?!\()'

        def replace_timestamp(match):
            timestamp = match.group(0)
            timestamp_url = create_youtube_timestamp_url(video_id, timestamp, offset_seconds=-10)
            return f"[{timestamp}]({timestamp_url})"

        summary_content = re.sub(timestamp_pattern, replace_timestamp, summary_content)

    # Rebuild full content
    new_content = new_header + summary_content

    # Write back
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    print(f"\n{'='*70}")
    print(f"STANDARDIZING ALL SUMMARY FILES")
    print(f"{'='*70}\n")

    # Load status
    print("→ Loading podcast status...")
    status_data = load_podcast_status()
    print("  ✓ Loaded")

    # Find all summaries
    summary_files = list(PODCAST_WORK_DIR.rglob("summary.md"))
    print(f"\n→ Found {len(summary_files)} summary files\n")

    updated_count = 0
    failed_count = 0

    for summary_path in summary_files:
        podcast_name = summary_path.parent.parent.name
        episode_name = summary_path.parent.name[:60]

        print(f"Processing: {podcast_name}/{episode_name}...")

        try:
            if standardize_summary(summary_path, status_data):
                print(f"  ✅ Standardized")
                updated_count += 1
            else:
                print(f"  ⚠️  Skipped")
                failed_count += 1
        except Exception as e:
            print(f"  ❌ Error: {e}")
            failed_count += 1

    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Total files: {len(summary_files)}")
    print(f"Standardized: {updated_count}")
    print(f"Failed/Skipped: {failed_count}")
    print(f"\n✅ All summaries standardized!")

if __name__ == "__main__":
    main()
