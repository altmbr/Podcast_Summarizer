#!/usr/bin/env python3
import os
import subprocess
import sys
import json
import time
import re
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
WHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large
PODCAST_WORK_DIR = Path("./podcast_work")
PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_STATUS_MD_FILE = Path("./podcast_status.md")
PROCESSING_LOCK_FILE = Path("./processing.lock")
SUMMARIZATION_PROMPT_FILE = Path("./summarization_prompt.md")
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"  # For summarization (latest Sonnet 4.5)
HAIKU_MODEL = "claude-3-5-haiku-20241022"  # For speaker identification (latest Haiku)

# Episode status states
STATUS_STATES = {
    "discovered": 1,      # Found in playlist, not downloaded yet
    "downloaded": 2,      # Audio file downloaded
    "transcribed": 3,     # Transcription completed
    "summarized": 4       # Summary generated
}

def acquire_lock(timeout=30):
    """Acquire a lock file to prevent parallel duplicate processing"""
    start_time = time.time()
    while PROCESSING_LOCK_FILE.exists():
        if time.time() - start_time > timeout:
            print("Warning: Lock file timeout - proceeding anyway")
            break
        time.sleep(0.5)

    # Create lock file
    PROCESSING_LOCK_FILE.write_text(str(os.getpid()))

def release_lock():
    """Release the lock file"""
    if PROCESSING_LOCK_FILE.exists():
        PROCESSING_LOCK_FILE.unlink()

def load_podcast_status():
    """Load podcast episode status tracking"""
    if PODCAST_STATUS_FILE.exists():
        with open(PODCAST_STATUS_FILE, 'r') as f:
            return json.load(f)
    return {"podcasts": {}}

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

def save_podcast_status(status_data):
    """Save podcast status to file (both JSON and markdown)"""
    with open(PODCAST_STATUS_FILE, 'w') as f:
        json.dump(status_data, f, indent=2)

    # Also generate markdown for readability
    generate_status_markdown(status_data)

def get_episode_status(status_data, podcast_url, video_id):
    """Get the current status of an episode"""
    podcast = status_data.get("podcasts", {}).get(podcast_url, {})
    episodes = podcast.get("episodes", {})
    episode = episodes.get(video_id, {})
    return episode.get("status", "discovered")

def set_episode_status(status_data, podcast_url, video_id, episode_title, new_status, upload_date=None):
    """Update the status of an episode"""
    if "podcasts" not in status_data:
        status_data["podcasts"] = {}
    if podcast_url not in status_data["podcasts"]:
        status_data["podcasts"][podcast_url] = {
            "podcast_name": None,
            "episodes": {}
        }
    if video_id not in status_data["podcasts"][podcast_url]["episodes"]:
        status_data["podcasts"][podcast_url]["episodes"][video_id] = {
            "title": episode_title,
            "upload_date": upload_date,  # YYYYMMDD format from YouTube
            "discovered_date": None,
            "status": "discovered"
        }

    episode = status_data["podcasts"][podcast_url]["episodes"][video_id]
    if episode["status"] == "discovered" and new_status != "discovered":
        episode["discovered_date"] = time.strftime("%Y-%m-%d %H:%M:%S")
    episode["status"] = new_status

    # Update podcast name if provided
    if status_data["podcasts"][podcast_url]["podcast_name"] is None:
        pass  # Will be set by the main function

def get_latest_downloaded_episode(status_data, podcast_url):
    """Get the most recently downloaded episode for a podcast (by upload_date)"""
    podcast = status_data.get("podcasts", {}).get(podcast_url, {})
    episodes = podcast.get("episodes", {})

    downloaded = [
        (vid, ep) for vid, ep in episodes.items()
        if ep.get("status") in ["downloaded", "transcribed", "summarized"]
    ]

    if not downloaded:
        return None

    # Sort by upload_date (descending) to get the newest
    downloaded.sort(key=lambda x: x[1].get("upload_date", "0"), reverse=True)
    return downloaded[0][0]

def load_summarization_prompt():
    """Load the customizable summarization prompt"""
    if SUMMARIZATION_PROMPT_FILE.exists():
        with open(SUMMARIZATION_PROMPT_FILE, 'r') as f:
            return f.read()
    # Fallback if file doesn't exist
    return """You are summarizing a podcast transcript. Focus on capturing who is saying what and include direct quotes.

Extract the key takeaways in a clear, concise format:

1. Main Topics (3-5 bullet points)
2. Key Insights (5-7 bullet points)
3. Key Quotes from Speakers (3-5 impactful quotes with speaker names)
4. Action Items or Recommendations (if any)

Keep it scannable and focused on substance."""

def show_recent_undownloaded_episodes(status_data, selected_podcast_urls=None):
    """Display all episodes from the last 30 days that haven't been downloaded"""
    from datetime import datetime, timedelta

    all_recent = []
    thirty_days_ago = datetime.now() - timedelta(days=30)

    for url, podcast_data in status_data.get('podcasts', {}).items():
        # Filter by selected podcasts if provided
        if selected_podcast_urls and url not in selected_podcast_urls:
            continue

        podcast_name = podcast_data.get('podcast_name', 'Unknown')
        episodes = podcast_data.get('episodes', {})

        for vid_id, episode in episodes.items():
            # Check if episode is not downloaded (status = discovered)
            if episode.get('status') == 'discovered':
                # Check upload date
                upload_date = episode.get('upload_date')
                if upload_date and len(upload_date) == 8:
                    try:
                        ep_date = datetime.strptime(upload_date, '%Y%m%d')
                        if ep_date >= thirty_days_ago:
                            all_recent.append({
                                'title': episode.get('title', 'Unknown'),
                                'upload_date': f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}",
                                'id': vid_id,
                                'podcast_name': podcast_name
                            })
                    except:
                        pass

    if not all_recent:
        print("No new episodes from the past 30 days.")
        return

    # Sort by upload date (newest first)
    all_recent.sort(key=lambda x: x['upload_date'], reverse=True)

    print(f"\n{'='*70}")
    print(f"📅 RECENT EPISODES (Last 30 days, not yet downloaded)")
    print(f"{'='*70}\n")

    episode_map = {}  # Map numbers to episode info for quick lookup

    for episode_number, ep in enumerate(all_recent, 1):
        title = ep['title'][:60]
        if len(ep['title']) > 60:
            title += "..."
        print(f"{episode_number}. [{ep['podcast_name']}] {ep['upload_date']} - {title}")
        episode_map[episode_number] = ep

    print()
    return episode_map

def show_episode_selection_menu(all_episodes_to_process):
    """Display all new episodes and let user select which ones to download"""
    if not all_episodes_to_process:
        print("✓ No new episodes found across all podcasts")
        return {}

    print(f"\n{'='*70}")
    print(f"📋 EPISODE SELECTION")
    print(f"{'='*70}")
    print(f"\nFound {len(all_episodes_to_process)} new episode(s) to download:\n")

    # Display all episodes with numbering
    for idx, (podcast_name, feed_url, video_info) in enumerate(all_episodes_to_process, 1):
        print(f"{idx}. [{podcast_name}]")
        print(f"   Title: {video_info['title'][:70]}")
        if len(video_info['title']) > 70:
            print(f"           {video_info['title'][70:]}")
        print(f"   Video ID: {video_info['id']}")
        print()

    # Get user selection
    while True:
        print("Options:")
        print("  'all'     - Download all episodes")
        print("  '1,2,3'   - Download specific episodes (comma-separated)")
        print("  'cancel'  - Cancel processing")
        print()

        user_input = input("Enter your selection: ").strip().lower()

        if user_input == "cancel":
            print("Cancelled. Exiting.")
            return {}

        if user_input == "all":
            # Return all episodes
            return {i: ep for i, ep in enumerate(all_episodes_to_process)}

        # Parse comma-separated numbers
        try:
            selected_indices = [int(x.strip()) - 1 for x in user_input.split(",")]
            # Validate indices
            if all(0 <= idx < len(all_episodes_to_process) for idx in selected_indices):
                return {i: all_episodes_to_process[idx] for i, idx in enumerate(selected_indices)}
            else:
                print("❌ Invalid selection. Please enter valid episode numbers.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter 'all', 'cancel', or comma-separated numbers.")
            continue

def extract_podcast_name_from_url(playlist_url):
    """Extract a readable podcast name from the playlist URL"""
    # Extract the list ID from the URL
    match = re.search(r'list=([A-Za-z0-9_-]+)', playlist_url)
    if match:
        list_id = match.group(1)
        return list_id[:20]  # Use first 20 chars of list ID as folder name
    return "unknown_podcast"

def sanitize_filename(filename):
    """Sanitize a string to be used as a valid filename"""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    return filename

def get_playlist_videos(playlist_url, first_run=False):
    """Get video URLs from a YouTube playlist with upload dates using efficient single call"""
    print(f"  → Fetching videos from playlist...")
    cmd = [
        "yt-dlp",
        "--flat-playlist",
        "-j",  # JSON output
        "--extractor-args", "youtubetab:approximate_date",  # Get upload dates in one call
        playlist_url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    videos = []
    for line in result.stdout.strip().split('\n'):
        if line:
            try:
                entry = json.loads(line)
                video_id = entry.get('id')
                video_title = entry.get('title', 'Unknown')
                upload_date = entry.get('upload_date', '0')  # YYYYMMDD format
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                videos.append({
                    'id': video_id,
                    'url': video_url,
                    'title': video_title,
                    'upload_date': upload_date
                })
            except json.JSONDecodeError:
                continue

    # Sort by upload_date in descending order (newest first)
    videos.sort(key=lambda x: x.get('upload_date', '0'), reverse=True)

    # On first run, only suggest the latest video
    if first_run and videos:
        print(f"  → First run detected - suggesting only the latest episode")
        return [videos[0]]  # Return the newest after sorting

    return videos

def download_video_audio(video_url, output_audio_path):
    """Download audio from URL using yt-dlp"""
    print(f"  → Downloading video audio...")
    # Create parent directories if needed
    output_audio_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "yt-dlp",
        "-x",  # Extract audio only
        "--audio-format", "mp3",
        "-o", str(output_audio_path),
        video_url
    ]
    subprocess.run(cmd, check=True)
    print(f"  ✓ Audio downloaded")

def transcribe_audio_to_text(audio_file_path, transcript_file_path):
    """Transcribe audio using standard Whisper with timestamps"""
    print(f"  → Transcribing audio to text (this may take a while)...")
    # Create parent directories if needed
    transcript_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Whisper will output as .json in the output directory
    audio_stem = audio_file_path.stem
    whisper_output_json = transcript_file_path.parent / f"{audio_stem}.json"

    cmd = [
        "whisper",
        str(audio_file_path),
        "--model", WHISPER_MODEL,
        "--output_dir", str(transcript_file_path.parent),
        "--output_format", "json",
        "--language", "en",
        "--verbose", "False"
    ]
    subprocess.run(cmd, check=True)

    # Read and parse JSON output
    with open(whisper_output_json, 'r') as f:
        whisper_data = json.load(f)

    # Format transcript with timestamps
    transcript_text = format_transcript_with_timestamps(whisper_data)

    # Write to file
    with open(transcript_file_path, 'w') as f:
        f.write(transcript_text)

    # Clean up
    whisper_output_json.unlink()

    print(f"  ✓ Transcription complete ({len(transcript_text)} characters)")
    return transcript_text



def format_transcript_with_timestamps(whisper_data):
    """Format standard Whisper JSON output with timestamps (no speaker info)"""
    formatted_lines = []

    if "segments" in whisper_data and len(whisper_data["segments"]) > 0:
        for segment in whisper_data["segments"]:
            # Extract timestamp and text
            start_time = segment.get("start", 0)
            end_time = segment.get("end", 0)
            text = segment.get("text", "").strip()

            if text:
                # Format timestamp as [HH:MM:SS]
                hours = int(start_time // 3600)
                minutes = int((start_time % 3600) // 60)
                seconds = int(start_time % 60)
                timestamp = f"[{hours:02d}:{minutes:02d}:{seconds:02d}]"

                formatted_line = f"{timestamp} {text}"
                formatted_lines.append(formatted_line)
        print(f"  → Found {len(whisper_data['segments'])} segments with timestamps")
    else:
        # Fallback if no segments available
        full_text = whisper_data.get("text", "")
        if full_text:
            formatted_lines.append(full_text)
            print(f"  ⚠ No segments available, using full text transcript (segments count: {len(whisper_data.get('segments', []))})")

    return "\n".join(formatted_lines)

def extract_video_metadata(video_url):
    """Extract metadata from YouTube video (title, description, channel)"""
    try:
        cmd = [
            "yt-dlp",
            "-j",  # JSON output
            "--no-warnings",
            video_url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            metadata = json.loads(result.stdout)
            return {
                "title": metadata.get("title", ""),
                "description": metadata.get("description", ""),
                "channel": metadata.get("channel", ""),
                "uploader": metadata.get("uploader", "")
            }
    except Exception as e:
        print(f"  ⚠ Could not extract metadata: {e}")
    return {"title": "", "description": "", "channel": "", "uploader": ""}

def parse_guest_names_from_description(description, title):
    """Parse guest names from video description and title using pattern matching"""
    guest_names = []

    if not description:
        return guest_names

    # Patterns to look for guest names in description
    patterns = [
        r"(?:Guest|Guests|Featuring|With|Interview with|Hosted by|Joined by)[\s:]*([^\n]+?)(?:\n|$)",
        r"(?:Guest|Guests|Featuring|With):\s*([^\n]+?)(?:\n|$)",
        r"In this episode.*?(?:with|featuring|interview)\s+([^\n]+?)(?:\.|,|$)",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, description, re.IGNORECASE)
        for match in matches:
            # Clean up the match
            names_text = match.strip()
            # Split by common delimiters
            for name in re.split(r'[,&]|and', names_text):
                name = name.strip()
                # Remove URLs and other junk
                name = re.sub(r'https?://[^\s]+', '', name).strip()
                # Remove common non-name suffixes
                name = re.sub(r'\s*\(.*?\)', '', name).strip()
                if name and len(name) > 2 and len(name) < 100:  # Reasonable name length
                    guest_names.append(name)

    return list(dict.fromkeys(guest_names))  # Remove duplicates while preserving order

def identify_and_replace_speakers(diarized_transcript, video_metadata, video_title):
    """Use Claude to identify speaker names and replace SPEAKER_XX placeholders"""
    print(f"  → Identifying speakers with AI...")

    try:
        from anthropic import Anthropic
    except ImportError:
        print("  ⚠ Anthropic SDK not installed. Install with: pip install anthropic")
        print("  → Skipping speaker identification")
        return diarized_transcript

    # Parse guest names from metadata
    guest_names = parse_guest_names_from_description(video_metadata.get("description", ""), video_title)

    # If we don't have guest names, try to extract from title
    if not guest_names and video_metadata.get("title"):
        guest_names = parse_guest_names_from_description(video_metadata.get("title", ""), "")

    # Build context for Claude
    metadata_context = f"""Video Title: {video_title}
Channel/Uploader: {video_metadata.get('uploader', 'Unknown')}
Possible Guests: {', '.join(guest_names) if guest_names else 'Not found in description'}"""

    # Create prompt for Claude to identify speakers
    identification_prompt = f"""I have a podcast transcript with speaker diarization labels (SPEAKER_00, SPEAKER_01, etc).
I need you to identify who these speakers are based on:
1. The dialogue context and what each speaker says about themselves
2. Possible guest names from the video metadata
3. Natural conversational cues

Metadata:
{metadata_context}

Transcript:
{diarized_transcript}

Your task:
1. Analyze the transcript to identify unique speakers
2. Match speakers to names based on context clues and metadata
3. Replace SPEAKER_XX labels with actual names (e.g., Sam, Sasha, etc)
4. If you cannot confidently identify a speaker, keep the SPEAKER_XX label
5. Return ONLY the updated transcript with speaker names - no other text

Keep the exact same format with timestamps and text, just replace speaker labels."""

    try:
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

        # Use streaming for long-context requests to avoid timeout
        updated_transcript = ""
        with client.messages.stream(
            model=CLAUDE_MODEL,
            max_tokens=25000,
            messages=[
                {"role": "user", "content": identification_prompt}
            ]
        ) as stream:
            for text in stream.text_stream:
                updated_transcript += text

        print(f"  ✓ Speaker identification complete")
        return updated_transcript

    except Exception as e:
        print(f"  ⚠ Speaker identification failed: {e}")
        print(f"  → Using original transcript with speaker placeholders")
        return diarized_transcript

def summarize_transcript_with_ai(transcript_text, video_title, custom_prompt):
    """Summarize transcript using Claude Sonnet 4.5"""
    print(f"  → Generating AI summary...")

    try:
        from anthropic import Anthropic
    except ImportError:
        print("  ⚠ Anthropic SDK not installed. Install with: pip install anthropic")
        return ""

    client = Anthropic()

    # Combine custom prompt with the transcript
    full_prompt = f"{custom_prompt}\n\n---\n\nTranscript:\n{transcript_text}"

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    summary_text = response.content[0].text
    print(f"  ✓ Summary generated")
    return summary_text

def process_single_video(video_info, video_index, podcast_name, podcast_url, custom_prompt, status_data):
    """Download, transcribe, identify speakers, and summarize a single video"""
    sanitized_episode_title = sanitize_filename(video_info['title'])
    video_id = video_info['id']

    print(f"\n  📹 Processing video {video_index}: '{video_info['title']}'")
    print(f"     Video ID: {video_id}")

    # Create episode folder and file paths
    episode_folder = PODCAST_WORK_DIR / podcast_name / sanitized_episode_title
    episode_folder.mkdir(parents=True, exist_ok=True)

    raw_podcast_path = episode_folder / "raw_podcast.mp3"
    transcript_raw_path = episode_folder / "transcript_raw.md"  # Before speaker identification
    transcript_path = episode_folder / "transcript.md"          # After speaker identification
    summary_path = episode_folder / "summary.md"

    # Step 1: Download
    if get_episode_status(status_data, podcast_url, video_id) == "discovered":
        print(f"  → Downloading...")
        download_video_audio(video_info['url'], raw_podcast_path)
        set_episode_status(status_data, podcast_url, video_id, video_info['title'], "downloaded")
        print(f"  ✓ Downloaded")
    else:
        print(f"  → Skipping download (already downloaded)")

    # Step 2: Transcribe (Whisper outputs .txt, we'll keep it)
    if get_episode_status(status_data, podcast_url, video_id) == "downloaded":
        print(f"  → Transcribing...")
        # Save to transcript_raw.md (before speaker identification)
        transcript_text = transcribe_audio_to_text(raw_podcast_path, transcript_raw_path)
        # Also save a copy to transcript.md for viewing (will be overwritten after speaker ID)
        with open(transcript_path, 'w') as f:
            f.write(transcript_text)
        set_episode_status(status_data, podcast_url, video_id, video_info['title'], "transcribed")
        print(f"  ✓ Transcribed")
    elif get_episode_status(status_data, podcast_url, video_id) in ["transcribed", "summarized"]:
        print(f"  → Skipping transcription (already transcribed)")
        # Read from raw transcript if available, otherwise from main transcript
        if transcript_raw_path.exists():
            with open(transcript_raw_path, 'r') as f:
                transcript_text = f.read()
        elif transcript_path.exists():
            with open(transcript_path, 'r') as f:
                transcript_text = f.read()
    else:
        transcript_text = ""
        print(f"  ⚠ Cannot transcribe - episode not downloaded")

    # Extract video metadata early (needed for both speaker identification and summary header)
    video_metadata = None
    guest_names = []
    if transcript_text:
        print(f"  → Extracting video metadata...")
        video_metadata = extract_video_metadata(video_info['url'])
        guest_names = parse_guest_names_from_description(
            video_metadata.get("description", ""),
            video_info['title']
        )

    # Step 3: Identify and replace speakers
    if transcript_text and get_episode_status(status_data, podcast_url, video_id) == "transcribed":
        print(f"  → Step 3: Identifying speakers...")
        # Identify speakers and replace SPEAKER_XX with actual names
        transcript_text = identify_and_replace_speakers(transcript_text, video_metadata, video_info['title'])
        # Update transcript file with speaker-identified version
        with open(transcript_path, 'w') as f:
            f.write(transcript_text)
        print(f"  ✓ Speaker identification complete")

    # Step 4: Summarize
    if transcript_text and get_episode_status(status_data, podcast_url, video_id) == "transcribed":
        print(f"  → Step 4: Generating summary...")
        summary_text = summarize_transcript_with_ai(transcript_text, video_info['title'], custom_prompt)
        set_episode_status(status_data, podcast_url, video_id, video_info['title'], "summarized")
        print(f"  ✓ Summarized")
    elif get_episode_status(status_data, podcast_url, video_id) == "summarized":
        print(f"  → Skipping summarization (already summarized)")
        return None, summary_path
    else:
        summary_text = ""
        print(f"  ⚠ Cannot summarize - episode not transcribed")
        return None, summary_path

    # Format upload date (YYYYMMDD -> Month DD, YYYY)
    formatted_date = "Unknown"
    if video_info.get('upload_date') and video_info['upload_date'] != '0':
        try:
            from datetime import datetime
            date_obj = datetime.strptime(video_info['upload_date'], '%Y%m%d')
            formatted_date = date_obj.strftime('%B %d, %Y')
        except:
            formatted_date = video_info['upload_date']

    # Write summary to file (with metadata header)
    with open(summary_path, 'w') as f:
        f.write(f"# {video_info['title']}\n\n")
        f.write(f"**Podcast:** {podcast_name}\n")
        f.write(f"**Date:** {formatted_date}\n")
        if guest_names:
            f.write(f"**Participants:** {', '.join(guest_names)}\n")
        f.write(f"**Video ID:** {video_id}\n")
        f.write(f"**Video URL:** {video_info['url']}\n")
        f.write(f"**Transcript:** ./transcript.md\n\n")
        f.write("---\n\n")
        f.write(summary_text)

    print(f"  ✓ Episode folder: {episode_folder}")
    print(f"  ✓ Raw podcast saved to: {raw_podcast_path}")
    print(f"  ✓ Transcript (raw) saved to: {transcript_raw_path}")
    print(f"  ✓ Transcript (with speaker IDs) saved to: {transcript_path}")
    print(f"  ✓ Summary saved to: {summary_path}")

    return summary_text, summary_path

def main():
    # Check for API key
    if not OPENAI_API_KEY:
        print("❌ Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)

    # Check for Anthropic API key for speaker identification
    anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        print("⚠ Note: ANTHROPIC_API_KEY not set - speaker identification will be skipped")
        print("   To enable: Set ANTHROPIC_API_KEY in your .env file")
    else:
        print("✓ Anthropic API is configured for speaker identification")

    # Load custom summarization prompt
    custom_prompt = load_summarization_prompt()

    # Acquire lock to prevent parallel duplicate processing
    acquire_lock()

    try:
        # Create main podcast work directory
        PODCAST_WORK_DIR.mkdir(exist_ok=True)

        # Load podcast status tracking
        status_data = load_podcast_status()

        # Read podcast URLs from file
        podcast_urls_file = Path("podcast_urls.txt")
        if not podcast_urls_file.exists():
            print(f"❌ Error: {podcast_urls_file} not found")
            print("   Create a file called 'podcast_urls.txt' with one URL per line")
            sys.exit(1)

        # Parse podcast URLs with optional names from comments
        podcast_feeds = []
        with open(podcast_urls_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Check if there's a comment with a podcast name
                if '#' in line and not line.startswith('#'):
                    url_part, name_part = line.split('#', 1)
                    feed_url = url_part.strip()
                    podcast_name = name_part.strip()
                else:
                    feed_url = line
                    podcast_name = None

                podcast_feeds.append((feed_url, podcast_name))

        if not podcast_feeds:
            print("❌ No podcast URLs found in podcast_urls.txt")
            sys.exit(1)

        print(f"\n📻 Starting podcast summarizer")
        print(f"   Found {len(podcast_feeds)} podcast feed(s) to check")
        print(f"   Status file: {PODCAST_STATUS_FILE}")
        print(f"   Using prompt from: {SUMMARIZATION_PROMPT_FILE}")

        # PHASE 1: Discover all new episodes across all podcasts
        print(f"\n{'='*70}")
        print(f"🔍 PHASE 1: Discovering new episodes...")
        print(f"{'='*70}")

        all_episodes_to_process = []  # Store (podcast_name, feed_url, video_info) tuples
        podcast_info_map = {}  # Store podcast metadata for later use

        # Process each podcast feed to discover new episodes
        for feed_url, custom_podcast_name in podcast_feeds:
            # Check if this is a YouTube playlist or a single video
            if 'playlist' in feed_url:
                print(f"📋 Checking playlist: {feed_url[:50]}...")

                # Use custom name if provided, otherwise extract from URL
                if custom_podcast_name:
                    podcast_name = custom_podcast_name
                else:
                    podcast_name = extract_podcast_name_from_url(feed_url)

                # Update podcast name in status
                if feed_url not in status_data["podcasts"]:
                    status_data["podcasts"][feed_url] = {"podcast_name": podcast_name, "episodes": {}}
                else:
                    status_data["podcasts"][feed_url]["podcast_name"] = podcast_name

                # Store for later use
                podcast_info_map[feed_url] = {
                    "podcast_name": podcast_name,
                    "custom_podcast_name": custom_podcast_name
                }

                # Check if this is the first time we're seeing this podcast
                is_first_run_for_this_podcast = len(status_data["podcasts"][feed_url]["episodes"]) == 0

                # Get all videos from the playlist
                playlist_videos = get_playlist_videos(feed_url, first_run=is_first_run_for_this_podcast)

                # Determine which videos to process
                if is_first_run_for_this_podcast:
                    # First run: suggest downloading only the latest (already filtered by get_playlist_videos)
                    videos_to_suggest = playlist_videos
                else:
                    # Subsequent runs: get videos after the latest downloaded one
                    latest_downloaded_id = get_latest_downloaded_episode(status_data, feed_url)
                    if latest_downloaded_id:
                        # Find the position of the latest downloaded and get all after it (newer episodes)
                        latest_index = next((i for i, v in enumerate(playlist_videos) if v['id'] == latest_downloaded_id), -1)
                        videos_to_suggest = playlist_videos[:latest_index] if latest_index >= 0 else []
                    else:
                        # No episodes downloaded yet, suggest only the latest
                        videos_to_suggest = playlist_videos[:1] if playlist_videos else []

                # Add all discovered videos to status (or update if previously private)
                for video_info in playlist_videos:
                    video_id = video_info['id']
                    existing_episode = status_data["podcasts"][feed_url]["episodes"].get(video_id)

                    # Add new episode OR update if it was previously private/unlisted
                    if not existing_episode:
                        set_episode_status(status_data, feed_url, video_id, video_info['title'], "discovered", video_info.get('upload_date'))
                    elif existing_episode.get('title') == '[Private video]' or existing_episode.get('upload_date') == '0':
                        # Update metadata for previously private videos that are now public
                        existing_episode['title'] = video_info['title']
                        existing_episode['upload_date'] = video_info.get('upload_date')
                        print(f"  → Updated metadata for previously private video: {video_info['title'][:60]}")

                # Add to selection list
                for video_info in videos_to_suggest:
                    all_episodes_to_process.append((podcast_name, feed_url, video_info))
            else:
                # Single video URL (not a playlist)
                print(f"▶️ Found single video: {feed_url[:50]}...")

                video_id = feed_url.split('v=')[-1]
                # Use custom name if provided, otherwise use default
                if custom_podcast_name:
                    podcast_name = custom_podcast_name
                else:
                    podcast_name = "single_videos"

                # Store for later use
                podcast_info_map[feed_url] = {
                    "podcast_name": podcast_name,
                    "custom_podcast_name": custom_podcast_name
                }

                video_info = {
                    'url': feed_url,
                    'id': video_id,
                    'title': 'Video'
                }
                all_episodes_to_process.append((podcast_name, feed_url, video_info))

        # Save discovered videos to status before selection
        save_podcast_status(status_data)

        # Show recent undownloaded episodes from the past 30 days (all podcasts)
        recent_episode_map = show_recent_undownloaded_episodes(status_data)

        # PHASE 2: Select from recent episodes
        if not recent_episode_map:
            print("No episodes to process. Exiting.")
            save_podcast_status(status_data)
            return

        print(f"\n{'='*70}")
        print(f"📋 PHASE 2: Select episodes to download")
        print(f"{'='*70}\n")
        print("Select from the recent episodes above:")
        print("  'all'     - Download all episodes")
        print("  '1,5,10'  - Download specific episode numbers (comma-separated)")
        print("  'cancel'  - Cancel processing\n")

        # Get user selection from recent episodes
        while True:
            user_input = input("Enter your selection: ").strip().lower()

            if user_input == "cancel":
                print("Cancelled. Exiting.")
                save_podcast_status(status_data)
                return

            if user_input == "all":
                selected_recent = recent_episode_map
                break

            # Parse comma-separated numbers
            try:
                selected_indices = [int(x.strip()) for x in user_input.split(",")]
                # Validate indices
                if all(idx in recent_episode_map for idx in selected_indices):
                    selected_recent = {idx: recent_episode_map[idx] for idx in selected_indices}
                    break
                else:
                    print("❌ Invalid selection. Please enter valid episode numbers from the list above.")
                    continue
            except ValueError:
                print("❌ Invalid input. Please enter 'all', 'cancel', or comma-separated numbers.")
                continue

        # Convert selected recent episodes to the format needed for processing
        selected_episodes = {}
        for idx, (number, episode_info) in enumerate(selected_recent.items()):
            podcast_name = episode_info['podcast_name']
            video_info = {
                'id': episode_info['id'],
                'url': f"https://www.youtube.com/watch?v={episode_info['id']}",
                'title': episode_info['title'],
                'upload_date': episode_info['upload_date']
            }
            # Find the podcast_url from status_data
            podcast_url = None
            for url, pdata in status_data.get('podcasts', {}).items():
                if pdata.get('podcast_name') == podcast_name:
                    podcast_url = url
                    break
            if podcast_url:
                selected_episodes[idx] = (podcast_name, podcast_url, video_info)

        if not selected_episodes:
            print("No episodes selected. Exiting.")
            save_podcast_status(status_data)
            return

        # PHASE 3: Process selected episodes
        print(f"\n{'='*70}")
        print(f"⏱️  PHASE 3: Processing {len(selected_episodes)} episode(s)...")
        print(f"{'='*70}")

        for idx, (podcast_name, feed_url, video_info) in selected_episodes.items():
            try:
                summary_text, summary_path = process_single_video(
                    video_info,
                    idx + 1,
                    podcast_name,
                    feed_url,
                    custom_prompt,
                    status_data
                )
                # Save after each successful video to handle interruptions
                save_podcast_status(status_data)
            except Exception as error:
                print(f"❌ Error processing '{video_info['title']}': {error}")
                import traceback
                traceback.print_exc()

        # Save final state
        save_podcast_status(status_data)

        print(f"\n{'='*60}")
        print(f"✓ All done!")
        print(f"   Episodes saved to: {PODCAST_WORK_DIR}")
        print(f"   Structure: podcast_work/[podcast_name]/[episode_name]/")
        print(f"     - raw_podcast.mp3")
        print(f"     - transcript.md")
        print(f"     - summary.md")
        print(f"   Status tracking saved to:")
        print(f"     - {PODCAST_STATUS_FILE} (for processing)")
        print(f"     - {PODCAST_STATUS_MD_FILE} (human-readable)")
        print(f"{'='*60}\n")

    finally:
        # Always release lock
        release_lock()

if __name__ == "__main__":
    main()
