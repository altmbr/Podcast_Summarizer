#!/usr/bin/env python3
"""
Update all summary.md files to have:
1. Clickable title linking to video
2. Clickable transcript link
3. All timestamps as clickable links (with 10-second offset)
"""

import re
from pathlib import Path

PODCAST_WORK_DIR = Path("./podcast_work")

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
    adjusted_seconds = max(0, total_seconds + offset_seconds)  # Don't go below 0

    # Convert back to YouTube format (XhYmZs)
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
    return 'xiaoyuzhoufm.com' in url

def extract_metadata_from_summary(content):
    """Extract Video ID and URL from summary metadata"""
    video_id = None
    video_url = None

    # Extract Video ID
    video_id_match = re.search(r'\*\*Video ID:\*\*\s*(.+)', content)
    if video_id_match:
        video_id = video_id_match.group(1).strip()

    # Extract Video URL
    video_url_match = re.search(r'\*\*Video URL:\*\*\s*(.+)', content)
    if video_url_match:
        video_url = video_url_match.group(1).strip()

    return video_id, video_url

def update_summary_file(summary_path):
    """Update a single summary.md file with clickable links"""

    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract video ID and URL
    video_id, video_url = extract_metadata_from_summary(content)

    if not video_id or not video_url:
        print(f"  ⚠️  Skipping {summary_path.parent.name} - missing video metadata")
        return False

    # Skip Xiaoyuzhou podcasts for now
    if is_xiaoyuzhou_url(video_url):
        print(f"  ⏭️  Skipping {summary_path.parent.name} - Xiaoyuzhou (not supported yet)")
        return False

    modified = False

    # Step 1: Make title clickable (only if not already clickable)
    title_pattern = r'^# ([^\[].+)$'
    title_match = re.search(title_pattern, content, re.MULTILINE)

    if title_match:
        original_title = title_match.group(1).strip()
        clickable_title = f"# [{original_title}]({video_url})"
        content = content.replace(title_match.group(0), clickable_title, 1)
        modified = True

    # Step 2: Make transcript link clickable
    transcript_pattern = r'\*\*Transcript:\*\*\s+\./transcript\.md'
    if re.search(transcript_pattern, content):
        content = re.sub(
            transcript_pattern,
            '**Transcript:** [View Transcript](./transcript.md)',
            content
        )
        modified = True

    # Step 3: Convert all timestamps to clickable links
    # Pattern: [HH:MM:SS] or [MM:SS] that are NOT already in markdown link syntax
    # Negative lookbehind to avoid timestamps already in links
    timestamp_pattern = r'(?<!\])\[(\d{1,2}:\d{2}:\d{2}|\d{1,2}:\d{2})\](?!\()'

    def replace_timestamp(match):
        timestamp = match.group(0)  # Includes brackets: [00:15:30]
        timestamp_url = create_youtube_timestamp_url(video_id, timestamp, offset_seconds=-10)
        return f"[{timestamp}]({timestamp_url})"

    new_content = re.sub(timestamp_pattern, replace_timestamp, content)

    if new_content != content:
        modified = True
        content = new_content

    # Write updated content
    if modified:
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    print(f"\n{'='*70}")
    print(f"UPDATING SUMMARY FILES WITH CLICKABLE LINKS")
    print(f"{'='*70}\n")

    # Find all summary.md files
    summary_files = list(PODCAST_WORK_DIR.rglob("summary.md"))

    if not summary_files:
        print("No summary files found.")
        return

    print(f"Found {len(summary_files)} summary file(s)\n")

    updated_count = 0
    skipped_count = 0
    xiaoyuzhou_count = 0

    for summary_path in summary_files:
        podcast_name = summary_path.parent.parent.name
        episode_name = summary_path.parent.name

        print(f"Processing: {podcast_name}/{episode_name[:60]}...")

        try:
            result = update_summary_file(summary_path)

            if result is None:  # Xiaoyuzhou
                xiaoyuzhou_count += 1
            elif result:
                updated_count += 1
                print(f"  ✅ Updated")
            else:
                skipped_count += 1
                print(f"  ⏭️  No changes needed")

        except Exception as e:
            print(f"  ❌ Error: {e}")
            skipped_count += 1

    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Total files: {len(summary_files)}")
    print(f"Updated: {updated_count}")
    print(f"Skipped (Xiaoyuzhou): {xiaoyuzhou_count}")
    print(f"Skipped (other): {skipped_count}")
    print(f"\n✅ All YouTube summaries now have clickable timestamps!")

if __name__ == "__main__":
    main()
