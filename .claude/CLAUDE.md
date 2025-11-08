# Podcast Summarizer System

A comprehensive podcast downloading, transcription, and summarization system that intelligently manages YouTube playlists with interactive episode selection.

## Overview

This system automates the process of:
1. Discovering new episodes from YouTube podcast playlists
2. Allowing you to interactively select which episodes to download
3. Downloading audio files
4. Transcribing audio to text using OpenAI's Whisper
5. Generating AI-powered summaries using GPT-4o-mini
6. Tracking episode status through the entire pipeline

## Architecture

### Directory Structure

```
project_root/
├── podcast_summarizer.py          # Main application script
├── podcast_urls.txt               # Configuration: list of podcast URLs
├── podcast_status.json            # State file: episode tracking
├── summarization_prompt.md        # Configuration: summary prompt template
├── .env                           # Configuration: API keys
├── processing.lock                # Runtime: lock file for parallel protection
├── .claude/
│   └── CLAUDE.md                  # This file - project memory
└── podcast_work/                  # Output directory
    └── [podcast_name]/            # One folder per podcast
        └── [episode_name]/        # One folder per episode
            ├── raw_podcast.mp3    # Downloaded audio file
            ├── transcript_raw.md  # Whisper transcription (before speaker ID)
            ├── transcript.md      # Transcript with speaker names
            └── summary.md         # AI-generated summary with metadata
```

### Episode Folder Structure Example

```
podcast_work/
└── 20VC/
    └── Joelle_Pineau_Scaling_Laws_AI_Success/
        ├── raw_podcast.mp3
        ├── transcript_raw.md         # Before speaker identification
        ├── transcript.md             # After speaker identification
        └── summary.md
```

## Configuration Files

### `podcast_urls.txt`

List of podcast URLs to track. Format: one URL per line with optional podcast name in comment.

**Example:**
```
https://www.youtube.com/playlist?list=PLnJFlI3aINuUNaznonoFEgMUGLBiLmB-w # 20VC
https://www.youtube.com/playlist?list=PLxxx # Tech Talk Weekly
https://www.youtube.com/watch?v=abc123 # Single Video
```

**Features:**
- Supports YouTube playlists
- Supports single video URLs
- Optional podcast name after `#` comment
- Lines starting with `#` are ignored
- Custom podcast names override automatic extraction

### Transcript Format

Transcripts now include **timestamps for each segment**:

**Example:**
```
[00:00:15] The scaling laws have been remarkably robust.
[00:00:45] There's a lot we don't know yet in terms of vulnerability.
[00:01:20] Today we have one of the leading minds in AI.
```

**Features:**
- `[HH:MM:SS]` timestamps for each transcribed segment
- Segments extracted from Whisper's JSON output
- Helps locate specific topics in the original audio
- Enables easy reference between transcript and video

### `summarization_prompt.md`

Customizable prompt that defines how episodes should be summarized. Designed for investor and entrepreneur audiences.

**Default Structure:**
- **Key Themes (3-10 themes)** - Main insights with substantiation
- **Contrarian Perspectives (3-5 perspectives)** - Non-obvious insights that challenge conventional wisdom
- **Companies Identified (3-10 companies)** - Companies mentioned for excellence or relevance
- **Operating Insights (1-5 insights)** - Tactical takeaways for operations and decision-making

### `podcast_status.json` & `podcast_status.md`

Master status tracking uses JSON for efficient processing and auto-generates a human-readable markdown file.

**JSON Structure:**
```json
{
  "podcasts": {
    "https://www.youtube.com/playlist?list=...": {
      "podcast_name": "20VC",
      "episodes": {
        "51y4KatMBFI": {
          "title": "Episode Title",
          "upload_date": "20241106",
          "discovered_date": "2024-11-06 22:31:00",
          "status": "summarized"
        }
      }
    }
  }
}
```

**Markdown File (`podcast_status.md`):**
- Auto-generated whenever status is saved
- Shows podcasts with episode counts and status breakdowns
- Each episode listed with:
  - Emoji indicators (✅ summarized, 📝 transcribed, ⬇️ downloaded, 🔍 discovered)
  - Publication date (from YouTube upload_date)
  - Processing status and discovery timestamp
- Human-readable for quick status checks

**Episode Status Values:**
- `discovered` - Found in playlist, not yet downloaded
- `downloaded` - Audio file downloaded to raw_podcast.mp3
- `transcribed` - Transcript generated via Whisper
- `summarized` - Summary generated via Claude Sonnet

### `.env`

Contains API keys and configuration.

**Required:**
```
OPENAI_API_KEY=sk-proj-...      # For GPT-4o-mini summarization and Whisper transcription
```

**Optional (for speaker identification):**
```
ANTHROPIC_API_KEY=sk-ant-...    # For Claude-based speaker name identification
```

With ANTHROPIC_API_KEY set, the system will identify speaker names from transcript context. The system will warn you at startup if this key is missing.

## Workflow

### Three-Phase Execution

When you run `python podcast_summarizer.py`:

#### Phase 1: Discovery (🔍)
- Scans all podcasts in `podcast_urls.txt`
- Fetches playlist contents
- Identifies new episodes:
  - **New podcasts**: Suggests only the latest episode
  - **Existing podcasts**: Suggests all episodes after the last downloaded one
- Updates `podcast_status.json` with all discovered episodes
- **No files are downloaded in this phase**

#### Phase 2: Interactive Selection (📋)
- **First**: Shows recent undownloaded episodes from the **last 30 days** across all podcasts
  - Numbered list for easy reference
  - Grouped by podcast name
  - Sorted by publication date (newest first)
  - Shows which ones are available to download
- **Then**: Displays numbered list of suggested episodes with:
  - Podcast name
  - Episode title
  - Video ID
- Prompts for user selection:
  - `all` - Select all suggested episodes
  - `1,2,3` - Select specific episodes (comma-separated numbers)
  - `cancel` - Exit without downloading

#### Phase 3: Processing (⏱️) - 4-Step Pipeline

For each selected episode:

**Step 1: Download**
- Extracts audio from YouTube video
- Saves as `raw_podcast.mp3`

**Step 2: Transcribe**
- Uses OpenAI's Whisper for transcription
- Includes segment timestamps `[HH:MM:SS]`
- Saves two versions:
  - `transcript_raw.md` - Before speaker identification (preserves full transcript if speaker ID fails)
  - `transcript.md` - Working copy (updated with speaker names in next step)

**Step 3: Identify Speakers**
- Extracts guest names from YouTube video description via regex patterns
- Uses Claude (Sonnet) to analyze dialogue context and identify speakers
- Replaces speaker labels with actual names where confident
- Handles edge cases where speaker names cannot be identified
- Updates transcript with speaker names

**Step 4: Summarize**
- Generates AI summary using GPT-4o-mini
- Includes speaker attribution in quotes and key points
- Formats with metadata header (title, podcast, URL, links to transcript)
- Saves as `summary.md`

Updates `podcast_status.json` after each episode completes.

### Smart Download Logic

**First Run (New Podcast)**
- Fetches all episodes from playlist
- Marks all as "discovered"
- **Suggests only the latest episode** to avoid overwhelming downloads
- Allows user to download just that 1 or modify selection

**Subsequent Runs (Existing Podcast)**
- Fetches all episodes from playlist
- Finds the latest episode with status ≥ "downloaded"
- **Suggests all episodes after that point**
- Allows user to select which new episodes to process

**Example Timeline:**
```
Day 1: Podcast has 10 episodes
  → Suggests episode 10 only
  → User downloads episode 10

Day 8: Podcast now has 13 episodes
  → Suggests episodes 11, 12, 13 (the new ones)
  → User downloads all 3 new episodes
```

## Dependencies

### Python Packages
```
openai           # GPT-4o-mini API for summarization
python-dotenv    # Load .env configuration
```

### System Tools
- `yt-dlp` - Download audio from YouTube
- `whisper` - Transcribe audio to text (OpenAI)
- `ffmpeg` - Audio processing

### API Keys
- OpenAI API key (for GPT-4o-mini and Whisper)

## Core Functions

### Status Management
- `load_podcast_status()` - Load status from JSON file
- `save_podcast_status(status_data)` - Save status to JSON file
- `get_episode_status(status_data, podcast_url, video_id)` - Get current status
- `set_episode_status(status_data, podcast_url, video_id, title, new_status)` - Update status with timestamp
- `get_latest_downloaded_episode(status_data, podcast_url)` - Find most recent completed episode

### Processing
- `process_single_video(video_info, video_index, podcast_name, podcast_url, custom_prompt, status_data)` - Download, transcribe, identify speakers, and summarize one episode (4-step pipeline)
- `download_video_audio(video_url, output_audio_path)` - Download audio via yt-dlp
- `transcribe_audio_to_text(audio_file_path, transcript_file_path)` - Transcribe via Whisper with segment timestamps
- `format_transcript_with_timestamps(whisper_data)` - Format Whisper JSON output with [HH:MM:SS] timestamps
- `extract_video_metadata(video_url)` - Extract title, description, channel, and uploader from YouTube video
- `parse_guest_names_from_description(description, title)` - Parse guest names from video description using regex patterns
- `identify_and_replace_speakers(transcript, video_metadata, video_title)` - Use Claude to identify speaker names from transcript context
- `summarize_transcript_with_ai(transcript_text, video_title, custom_prompt)` - Summarize via Claude Sonnet with the custom prompt

### Utility
- `extract_podcast_name_from_url(playlist_url)` - Extract podcast name from URL
- `sanitize_filename(filename)` - Remove invalid filename characters
- `show_episode_selection_menu(all_episodes_to_process)` - Interactive selection interface
- `get_playlist_videos(playlist_url, first_run)` - Fetch videos from playlist via yt-dlp

### File Management
- `load_summarization_prompt()` - Load custom prompt from file
- `acquire_lock()` / `release_lock()` - Prevent parallel processing conflicts

## Key Features

### Atomic Operations
- Status saved after every episode completes
- Can safely interrupt and resume without losing work
- No duplicate processing possible

### Smart Defaults
- First run: Downloads only latest to avoid overwhelming
- Subsequent runs: Only suggests new episodes
- Can always override and select manually

### Parallel Safety
- File-based locking prevents duplicate downloads
- 30-second lock timeout for stale locks
- Single instance guarantee

### Date Tracking
- Records when each episode was first discovered
- Provides audit trail of processing timeline
- Helps understand processing history

### Flexible Selection
- Download all new episodes at once
- Cherry-pick specific episodes
- Skip low-interest content
- Cancel anytime before processing starts

### Resumable Processing
- If download fails, transcript is already saved
- If transcription fails, download is already saved
- Resume from any point without re-processing

## Usage Examples

### Basic Usage
```bash
python podcast_summarizer.py
```

Then respond to the interactive prompts:
1. View discovered episodes
2. Enter selection (e.g., `all`, `1,3,5`, or `cancel`)
3. Wait for processing to complete

### First Time with a Podcast
```
1. Add URL to podcast_urls.txt with # Name
2. Run script
3. Script discovers all episodes, suggests latest
4. User can accept the 1 episode or modify selection
5. Episode gets downloaded, transcribed, summarized
```

### Adding New Episodes to Existing Podcast
```
1. Run script (no changes to podcast_urls.txt needed)
2. Script discovers all episodes, suggests only new ones
3. User selects which new episodes to process
4. Only those episodes are downloaded and processed
```

### Selective Processing
```
1. Run script (discovers 5 new episodes across 2 podcasts)
2. See all 5 listed with podcast names
3. Enter "1,3,5" to process only those 3
4. Episodes 2 and 4 are skipped
5. Status updated only for episodes 1, 3, 5
```

## File Naming

Episode folders use human-readable names derived from video titles:
- Spaces and special characters converted to underscores
- Invalid filename characters removed
- Example: "Joelle Pineau: Why Scaling Laws..." → "Joelle_Pineau_Scaling_Laws_AI_Success"

## Monitoring Progress

Check `podcast_status.json` to see current state:
```json
{
  "20VC": {
    "51y4KatMBFI": {
      "status": "summarized",
      "discovered_date": "2024-11-06 22:31:00"
    },
    "abc123xyz": {
      "status": "transcribed",
      "discovered_date": "2024-11-07 10:15:00"
    }
  }
}
```

## Configuration Customization

### Change Summary Format
Edit `summarization_prompt.md` to modify:
- What sections to include
- Level of detail
- Output structure
- Focus areas

The changes apply to all future summarizations.

### Change Whisper Model
In `podcast_summarizer.py`, modify:
```python
WHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large
```

Options trade off accuracy vs. speed/memory.

### Change LLM Model
In `podcast_summarizer.py`, modify the `summarize_transcript_with_ai()` function:
```python
model="gpt-4o-mini"  # Can change to other models
```

## Error Handling

- Failed downloads don't block transcription of other episodes
- Failed transcriptions don't block summaries of other episodes
- Errors are logged with full stack traces
- Status remains consistent even if errors occur
- Can safely retry failed episodes by re-running script

## Logging & Output

The script provides clear output:
- Discovery phase shows what's being checked
- Selection phase shows numbered list with details
- Processing phase shows progress for each step
- Errors include context and suggest fixes

## Backfilling Publication Dates

Episodes discovered before the upload_date feature was added don't have publication dates in the status file. To backfill these:

```bash
# Run the backfill script to fetch upload_date from YouTube for all episodes
python3 backfill_dates.py
```

This will:
- Iterate through all episodes without upload_date
- Fetch metadata from YouTube for each
- Store the upload_date (YYYYMMDD format)
- Update the markdown file with publication dates

Note: This can take a while for large podcast libraries (438+ episodes). The script is safe to interrupt and resume.

## Troubleshooting

### "OPENAI_API_KEY not set"
- Add `OPENAI_API_KEY=sk-...` to `.env` file
- Ensure `.env` is in the project root

### "yt-dlp not found"
- Install: `pip install yt-dlp`
- Or: `brew install yt-dlp` (macOS)

### "ffmpeg not found"
- Install: `brew install ffmpeg` (macOS)
- Or appropriate package manager for your OS

### "whisper not found"
- Install: `pip install openai-whisper`

### Script appears to hang
- Check if it's waiting for user input in Phase 2
- Press Ctrl+C to cancel

### Duplicate downloads despite running script
- Ensure no other instances are running
- Delete `processing.lock` if stale

## Advanced Usage

### Process Specific Episodes Only
1. Run script normally
2. At selection prompt, enter: `1,3,5` (just these episode numbers)
3. Script processes only those episodes

### Modify Individual Prompts
Edit `summarization_prompt.md` to change summary behavior for next run. Changes apply globally.

### Inspect Episode Status
```bash
cat podcast_status.json | python -m json.tool
```

View which episodes are at which stage of processing.

### Manual Resume
If a run is interrupted:
1. Check `podcast_status.json` for current state
2. Run script again
3. It will skip already-completed steps
4. Can modify selection to focus on incomplete episodes

## Future Enhancements

Potential improvements:
- Web UI for selection and monitoring
- Batch scheduling (process every N days)
- Email notifications on completion
- Support for RSS feeds
- Integration with note-taking apps
- Advanced filtering and search
- Statistics and analytics

## License & Attribution

Built with:
- OpenAI (Whisper, GPT-4o-mini)
- yt-dlp (YouTube downloading)
- Python community libraries
