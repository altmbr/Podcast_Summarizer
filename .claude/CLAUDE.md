# Podcast Summarizer System

A comprehensive podcast downloading, transcription, and summarization system that intelligently manages YouTube playlists with interactive episode selection.

## Overview

This system automates the process of:
1. Discovering new episodes from YouTube podcast playlists (including Chinese Xiaoyuzhou platform)
2. Allowing you to interactively select which episodes to process
3. Downloading audio files
4. Transcribing audio to text using OpenAI's Whisper
5. Identifying speakers using voice diarization and Claude AI
6. Generating comprehensive AI-powered summaries using Claude Sonnet 4.5 (16K tokens)
7. Automatically translating Chinese titles to English and tracking content region
8. Tracking episode status through the entire pipeline

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

### Standardized summary.md Format

All summary files follow this standardized format:

**YouTube Episodes:**
```markdown
# [Episode Title](https://www.youtube.com/watch?v=VIDEO_ID)

**Podcast:** Podcast Name
**Date:** Month DD, YYYY
**Participants:** Speaker 1, Speaker 2
**Region:** Western
**Video ID:** VIDEO_ID
**Video URL:** https://www.youtube.com/watch?v=VIDEO_ID
**Transcript:** [View Transcript](./transcript.md)

---

[Summary content with clickable timestamps]
```

**Xiaoyuzhou Episodes (Chinese):**
```markdown
# Episode Title

**Podcast:** Podcast Name
**Date:** Month DD, YYYY
**Participants:** Speaker 1, Speaker 2
**Region:** Chinese
**Video ID:** EPISODE_ID
**Video URL:** https://www.xiaoyuzhoufm.com/episode/EPISODE_ID
**Transcript:** [View Transcript](./transcript.md)

---

[Summary content]
```

**Key Features:**
- **Clickable title** (YouTube only) - Links directly to video
- **Clickable timestamps** (YouTube only) - All timestamps like `[00:15:30]` link to video at that moment (minus 10 seconds)
- **Standardized metadata** - Consistent fields across all episodes
- **Date formatting** - Human-readable format (e.g., "November 10, 2025")
- **Region tracking** - "Western" or "Chinese" for content categorization
- **Clickable transcript link** - "View Transcript" links to transcript.md

**Timestamp Linking:**
- YouTube timestamps automatically link with 10-second offset
- Format: `[[00:15:30]](https://www.youtube.com/watch?v=VIDEO_ID&t=15m20s)`
- Renders as clickable: [00:15:30] (user clicks timestamp to jump to video)
- Xiaoyuzhou timestamps remain as plain text (platform limitations)

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

**Recent Updates:**
- Chinese content is automatically translated to English in summaries
- Timestamps are now required for all quotes in format: "Quote here" [HH:MM:SS]
- Summaries can now be up to 16K tokens (previously 2K) for more comprehensive coverage

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
          "status": "summarized",
          "region": "Western"
        }
      }
    }
  }
}
```

**New Fields:**
- `region` - Either "Chinese" or "Western", automatically detected based on title language
  - Chinese titles are automatically translated to English and stored in the `title` field
  - Original Chinese titles are used for folder naming but translated for display

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
OPENAI_API_KEY=sk-proj-...       # For Whisper transcription only
ANTHROPIC_API_KEY=sk-ant-...     # For speaker identification (Haiku) and summarization (Sonnet 4.5)
```

The system requires both API keys:
- **OPENAI_API_KEY**: Used exclusively for Whisper audio transcription
- **ANTHROPIC_API_KEY**: Used for both speaker identification (Claude Haiku 3.5) and summarization (Claude Sonnet 4.5)

The system will warn you at startup if either key is missing.

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
- **First**: Shows recent incomplete episodes from the **last 30 days** across all podcasts
  - Incomplete episodes include: discovered, downloaded, or transcribed (not yet summarized)
  - Status indicator emoji (🔍 discovered, ⬇️ downloaded, 📝 transcribed)
  - Numbered list for easy reference
  - Grouped by podcast name
  - Sorted by publication date (newest first)
  - Shows translated titles for Chinese content
- **Then**: Displays numbered list of suggested episodes with:
  - Podcast name
  - Episode title (translated if Chinese)
  - Video ID
- Prompts for user selection:
  - `all` - Select all suggested episodes
  - `1,2,3` - Select specific episodes (comma-separated numbers)
  - `cancel` - Exit without processing

#### Phase 3: Processing (⏱️) - 4-Step Pipeline

For each selected episode:

**Step 1: Download**
- Extracts audio from YouTube video
- Saves as `raw_podcast.mp3`

**Step 2: Transcribe**
- Uses OpenAI's Whisper for transcription
- Includes segment timestamps `[HH:MM:SS]`
- Adds metadata header (title, podcast, date, URL)
- Saves initial transcript to `transcript_raw.md`

**Step 2a: Voice-Based Speaker Diarization** (if HuggingFace token configured)
- Uses pyannote.audio for voice-based speaker detection
- Adds speaker labels (SPEAKER_00, SPEAKER_01, etc.) based on voice analysis
- Runs locally on your machine (no API costs)
- Gracefully skips if not configured

**Step 3: Identify Speaker Names**
- Extracts guest names from YouTube video description via regex patterns (used as hints)
- Uses Claude Haiku to analyze first 15 minutes of transcript
- Maps SPEAKER_XX labels to actual full names using context and metadata
- Replaces speaker labels with actual names where confident
- Returns both updated transcript AND list of identified speaker names
- Updates transcript.md with speaker-identified version
- Identified speakers are used for the Participants field in summary

**Step 4: Summarize**
- Generates comprehensive AI summary using Claude Sonnet 4.5 (16,000 max tokens)
- Includes speaker attribution with **full names** in quotes and key points
- Includes timestamps in quotes (e.g., "Quote here" [00:15:30])
- Formats with metadata header including Participants and Region fields
- Metadata includes: title, podcast, date, participants, region (Chinese/Western), video ID, URL, transcript link
- Saves as `summary.md`

Updates `podcast_status.json` after each episode completes.

### Chinese Podcast Support

**Automatic Title Translation:**
- When an episode title contains Chinese characters, it is automatically detected
- The title is translated to English using Claude Haiku (cost-efficient)
- The translated title is stored in `podcast_status.json` for consistency
- Original Chinese title may still appear in folder names

**Region Tracking:**
- Each episode is tagged as either "Chinese" or "Western" based on title
- Region field is stored in `podcast_status.json` and `summary.md`
- Helps filter and organize content by language/region

**Xiaoyuzhou Platform:**
- Full support for Xiaoyuzhou (小宇宙) Chinese podcast platform
- Audio download via direct URL extraction
- Episode metadata and listing support
- See `xiaoyuzhou_helper.py` for implementation details

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
openai           # Whisper transcription API
anthropic        # Claude API for speaker identification and summarization
python-dotenv    # Load .env configuration
pyannote.audio   # Voice-based speaker diarization (optional but recommended)
```

### System Tools
- `yt-dlp` - Download audio from YouTube
- `whisper` - Transcribe audio to text (OpenAI)
- `ffmpeg` - Audio processing

### API Keys
- **OpenAI API key** - For Whisper transcription
- **Anthropic API key** - For speaker identification (Haiku 3.5) and summarization (Sonnet 4.5)
- **HuggingFace token** (optional) - For pyannote speaker diarization

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
- `summarize_transcript_with_ai(transcript_text, video_title, custom_prompt)` - Summarize via Claude Sonnet 4.5 with the custom prompt (16K token output)

### Chinese Language Support
- `has_chinese_characters(text)` - Detect if text contains Chinese characters (CJK Unicode range)
- `translate_chinese_to_english(text)` - Translate Chinese text to English using Claude Haiku
- Region detection and tracking automatically applied during episode discovery

### Utility
- `extract_podcast_name_from_url(playlist_url)` - Extract podcast name from URL
- `sanitize_filename(filename)` - Remove invalid filename characters
- `show_episode_selection_menu(all_episodes_to_process)` - Interactive selection interface (legacy, for new episodes)
- `show_recent_incomplete_episodes(status_data, selected_podcast_urls)` - Show incomplete episodes from last 30 days
- `get_playlist_videos(playlist_url, first_run)` - Fetch videos from playlist via yt-dlp

### Xiaoyuzhou Platform Support
See `xiaoyuzhou_helper.py` for Chinese podcast platform integration:
- `is_xiaoyuzhou_url(url)` - Check if URL is from Xiaoyuzhou platform
- `get_xiaoyuzhou_podcast_episodes(podcast_url, first_run)` - Fetch episode list
- `download_xiaoyuzhou_audio(episode_url, output_path)` - Download audio file
- `extract_xiaoyuzhou_podcast_name(podcast_url)` - Extract podcast name

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

### Change Summary Output Length
In `podcast_summarizer.py`, modify the `summarize_transcript_with_ai()` function:
```python
max_tokens=16000  # Current: 16K for comprehensive summaries
                  # Previous: 2K (increase provides much more detail)
```

Note: The system now uses Claude Sonnet 4.5 with 16K max tokens for more comprehensive summaries compared to the previous 2K limit.

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

## Cost Estimates

### Per Episode Processing Costs

**With Voice-Based Diarization (Recommended):**
- Transcription (Whisper): ~$0.10-0.30
- Diarization (pyannote, local): $0.00 (runs locally)
- Speaker ID (Claude Haiku, 15 min): ~$0.05-0.20
- Title Translation (Claude Haiku, if Chinese): ~$0.01-0.03
- Summarization (Claude Sonnet 4.5, 16K tokens): ~$0.30-1.50
- **Total: ~$0.45-2.00 per episode**

**Without Voice-Based Diarization:**
- Transcription (Whisper): ~$0.10-0.30
- Speaker ID (Claude Haiku, 15 min): ~$0.05-0.20 (less accurate without SPEAKER_XX labels)
- Title Translation (Claude Haiku, if Chinese): ~$0.01-0.03
- Summarization (Claude Sonnet 4.5, 16K tokens): ~$0.30-1.50
- **Total: ~$0.45-2.00 per episode**

**Cost Considerations:**
- Using Haiku (not Sonnet) for speaker ID and translation: ~10x cheaper
- Using first 15 minutes only for speaker ID: ~3-4x fewer tokens
- Voice-based diarization: More accurate, no added API costs
- Increased summary length (2K → 16K tokens): More comprehensive, ~50% higher cost per episode
- Chinese title translation adds minimal cost (~$0.01-0.03 per episode)

### Monthly Cost Examples

- **Light usage** (10 episodes/month): $4.50-20.00
- **Medium usage** (50 episodes/month): $22.50-100.00
- **Heavy usage** (200 episodes/month): $90-400

Note: Costs vary based on:
- Episode length (longer = more transcription cost)
- Transcript complexity (affects summarization tokens)
- Number of speakers (minimal impact with voice diarization)

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
