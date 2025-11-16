# Podcast Summarizer

A comprehensive podcast downloading, transcription, and summarization system that intelligently manages YouTube playlists with interactive episode selection.

**🌐 Live at [teahose.com](https://teahose.com)** - All summaries automatically published online via GitHub deployment.

## Features

- 🎙️ **Automated Discovery**: Tracks YouTube podcast playlists and detects new episodes
- 📥 **Interactive Selection**: Choose which incomplete episodes to process from the last 30 days
- 🎵 **Audio Download**: Extracts audio from YouTube videos (including Xiaoyuzhou Chinese podcasts)
- ⚡ **GPU-Accelerated Transcription**: Uses mlx-whisper for fast transcription on Apple Silicon
- 🗣️ **Voice-Based Speaker Diarization**: Uses pyannote.audio for accurate speaker detection (local, no API cost)
- 👥 **Speaker Identification**: Uses Claude Haiku to identify speaker names from context
- 📊 **Smart Summarization**: Generates comprehensive investor-focused summaries with Claude Sonnet 4.5 (16K token output)
- 🎨 **AI-Generated Header Images**: Creates vintage newspaper-style comic headers for weekly summaries with GPT-image-1
- 📰 **Weekly Digest**: Automatically generates weekly summaries with top 10 themes
- 🌏 **Chinese Podcast Support**: Automatic title translation and full integration with Xiaoyuzhou platform
- 🏷️ **Region Tracking**: Automatically detects and tracks Chinese vs Western content
- 🌐 **Auto-Publishing**: Push to GitHub, automatically deploys to teahose.com
- 💾 **State Management**: Tracks episode status through the entire pipeline
- 🔄 **Resumable**: Safe to interrupt and resume without re-processing

## Web Publishing

**All content is automatically published to the web:**

- 🌐 **Live Site**: [teahose.com](https://teahose.com)
- 🚀 **Auto-Deploy**: Push to GitHub → automatic deployment
- 📄 **Public Access**: All summaries, transcripts, and weekly digests
- 🖼️ **Images Included**: Header images and all visual content display online
- ⚡ **No Manual Steps**: Just `git push` and your content goes live

The repository is connected to a hosting service that automatically rebuilds and deploys the site whenever you push changes to GitHub. No configuration or manual deployment needed.

## Quick Start

### Prerequisites

**Required:**
- Python 3.8+
- ffmpeg
- yt-dlp
- OpenAI API key (for Whisper transcription)
- Anthropic API key (for speaker ID and summarization)

**Optional but Recommended:**
- Apple Silicon Mac (for GPU-accelerated transcription)
- HuggingFace token (for voice-based speaker diarization)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd podcast-summarizer
   ```

2. **Install Python dependencies**
   ```bash
   pip install openai python-dotenv anthropic mlx-whisper
   ```

3. **Install optional dependencies (recommended)**
   ```bash
   # For voice-based speaker diarization
   pip install pyannote.audio

   # Get HuggingFace token from https://huggingface.co/settings/tokens
   # Accept terms at https://huggingface.co/pyannote/speaker-diarization-3.1
   ```

4. **Install system tools**

   macOS:
   ```bash
   brew install ffmpeg yt-dlp
   ```

   Linux:
   ```bash
   sudo apt-get install ffmpeg
   pip install yt-dlp
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys (OPENAI_API_KEY, ANTHROPIC_API_KEY)
   # Optionally add HUGGINGFACE_TOKEN for speaker diarization
   ```

6. **Configure podcast URLs**
   ```bash
   cp podcast_urls.txt.example podcast_urls.txt
   # Edit podcast_urls.txt and add your podcast URLs
   ```

7. **Run the script**
   ```bash
   python podcast_summarizer.py
   ```

## Usage

### Basic Workflow

1. The script scans all podcasts in `podcast_urls.txt`
2. Shows you incomplete episodes (discovered/downloaded/transcribed) from the last 30 days
3. You select which episodes to process (or choose "all")
4. For each episode:
   - Downloads audio
   - Transcribes with mlx-whisper (GPU-accelerated)
   - Runs voice-based speaker diarization (if configured)
   - Identifies speaker names with Claude Haiku
   - Generates comprehensive summary with Claude Sonnet 4.5 (16K tokens)
   - Automatically translates Chinese titles to English
   - Tracks episode region (Chinese/Western)

### Episode Selection

When prompted, you can:
- Type `all` to process all suggested episodes
- Type `1,3,5` to process specific episodes (comma-separated)
- Type `cancel` to exit without processing

### Weekly Summary Generation

Generate a comprehensive weekly digest with AI-generated header image:

```bash
python generate_weekly_summary.py
```

This will:
1. Find all episodes published in the last 7 days
2. Generate a comprehensive summary with Claude Sonnet 4.5
3. Extract the top 10 themes from the summary
4. Create a vintage newspaper-style header image (10 panels, portrait layout)
5. Insert the image at the top of the markdown file (email-ready)
6. Save to `weekly_summaries/weekly_summary_YYYY-MM-DD_to_YYYY-MM-DD.md`

**Header Image Features:**
- 🎨 Vintage 1950s comic book style with Ben Day dots
- 📱 Portrait orientation (1024x1536) optimized for mobile
- 🖼️ 10 panels in 5x2 grid showing key themes
- 🤖 Generated with OpenAI's GPT-image-1 model
- ✉️ Perfect for email newsletters

**Manual header generation:**
```bash
# From existing summary
python generate_weekly_header_image.py \
  --summary weekly_summaries/weekly_summary_2025-11-04_to_2025-11-11.md \
  --output header.png

# From custom themes
python generate_weekly_header_image.py \
  --themes "AI Development" "Enterprise Sales" "VC Trends" \
           "Product Strategy" "Talent" "Healthcare" \
           "Finance" "Media" "Policy" "Culture" \
  --date "2025-11-04_to_2025-11-11" \
  --output header.png
```

### Output Structure

```
podcast_work/
└── [podcast_name]/
    └── [episode_name]/
        ├── raw_podcast.mp3           # Downloaded audio
        ├── transcript_raw.md         # Original transcript
        ├── transcript.md             # With speaker names
        └── summary.md                # AI-generated summary
```

## Configuration

### API Keys

Required in `.env`:
- `OPENAI_API_KEY` - For Whisper transcription
- `ANTHROPIC_API_KEY` - For speaker identification (Haiku) and summarization (Sonnet 4.5)

Optional in `.env`:
- `HUGGINGFACE_TOKEN` - For voice-based speaker diarization (highly recommended for accuracy)

### Podcast URLs

Add to `podcast_urls.txt`:
```
https://www.youtube.com/playlist?list=PLxxx # Podcast Name
```

### Summarization Prompt

Customize `summarization_prompt.md` to change summary format and focus areas.

### Whisper Model

In `podcast_summarizer.py`, line 17:
```python
WHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large
```

## Summary Format

All episode summaries follow a standardized format with clickable elements:

### YouTube Episodes
```markdown
# [Episode Title](https://www.youtube.com/watch?v=VIDEO_ID)

**Podcast:** Podcast Name
**Date:** November 10, 2025
**Participants:** Speaker 1, Speaker 2
**Region:** Western
**Video ID:** VIDEO_ID
**Video URL:** https://www.youtube.com/watch?v=VIDEO_ID
**Transcript:** [View Transcript](./transcript.md)

---

[Summary with clickable timestamps like [00:15:30]]
```

**Features:**
- **Clickable title** - Click to open the YouTube video
- **Clickable timestamps** - Click any timestamp to jump to that moment (10 seconds earlier)
- **Clickable transcript link** - Quick access to full transcript
- **Standardized metadata** - Consistent across all episodes

### Xiaoyuzhou Episodes (Chinese)
Same format but:
- Title is plain text (not clickable)
- Timestamps are plain text (platform limitation)
- Region shows "Chinese"

## Advanced Features

### Utility Scripts

- **`backfill_dates.py`** - Backfills publication dates for old episodes
- **`cleanup_incomplete.py`** - Removes incomplete episode folders and resets status
- **`create_summaries_html.py`** - Compile all summaries into styled HTML for web viewing
- **`create_summaries_pdf.py`** - Generate PDF compilation of summaries via pandoc
- **`generate_weekly_summary.py`** - Generates weekly digest of summaries from recently published episodes with AI header image
- **`generate_weekly_header_image.py`** - Creates vintage newspaper-style comic headers for weekly summaries (10 panels, portrait)
- **`generate_pithy_weekly_summary.py`** - Creates condensed version of weekly summary (40-50% reduction)
- **`standardize_all_summaries.py`** - Ensures all summary files have consistent format
- **`update_summary_timestamps.py`** - Adds clickable timestamps to existing summaries
- **`summarize_single_episode.py`** - Re-process/re-summarize individual episodes
- **`xiaoyuzhou_helper.py`** - Helper functions for Chinese podcast platform (Xiaoyuzhou) support

### Status Tracking

The system maintains two status files:
- `podcast_status.json` - Machine-readable state
- `podcast_status.md` - Human-readable overview

### Parallel Safety

File-based locking prevents duplicate processing if you accidentally run multiple instances.

## Cost Estimates

### Per Episode Processing
- Transcription (Whisper): $0.10-0.30
- Diarization (pyannote, local): $0.00 (runs locally on your machine)
- Speaker ID (Claude Haiku, 15 min): $0.05-0.20
- Summarization (Claude Sonnet 4.5, 16K tokens): $0.30-1.50
- Title Translation (if Chinese): $0.01-0.03
- **Total: ~$0.45-2.00 per episode**

### Per Weekly Summary
- Claude Sonnet 4.5 summarization (10-20 episodes): $0.50-2.00
- Header image generation (GPT-image-1): $0.04-0.08
- **Total: ~$0.54-2.08 per weekly summary**

### Monthly Costs (Medium Usage)
- 50 episodes: $22.50-100.00
- 4 weekly summaries: $2.16-8.32
- **Total: ~$24.66-108.32/month**

**Cost savings vs previous version:** 50-60% reduction through:
- Using Haiku instead of Sonnet for speaker ID (10x cheaper)
- Analyzing only first 15 minutes for speaker ID (3-4x fewer tokens)
- Local voice diarization (no API costs)

## Troubleshooting

### "OPENAI_API_KEY not set"
Add your key to the `.env` file.

### "yt-dlp not found"
Install with `pip install yt-dlp` or `brew install yt-dlp`.

### "ffmpeg not found"
Install with `brew install ffmpeg` (macOS) or `apt-get install ffmpeg` (Linux).

### "mlx-whisper not found"
Install with `pip install mlx-whisper`. Note: mlx-whisper requires Apple Silicon (M1/M2/M3).

### "pyannote.audio not found"
Install with `pip install pyannote.audio`. This is optional but recommended for better speaker detection.

### Script hangs
Check if it's waiting for input. Press Ctrl+C to cancel.

## Project Documentation

See `.claude/CLAUDE.md` for comprehensive technical documentation including:
- Detailed architecture
- File formats and structure
- Function reference
- Configuration options
- Future enhancement ideas

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license here]

## Acknowledgments

Built with:
- [mlx-whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper) - GPU-accelerated audio transcription for Apple Silicon
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) - Voice-based speaker diarization
- [Claude AI](https://www.anthropic.com/claude) - Speaker identification (Haiku) and summarization (Sonnet 4.5)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloading
