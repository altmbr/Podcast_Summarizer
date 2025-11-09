# Podcast Summarizer

A comprehensive podcast downloading, transcription, and summarization system that intelligently manages YouTube playlists with interactive episode selection.

## Features

- 🎙️ **Automated Discovery**: Tracks YouTube podcast playlists and detects new episodes
- 📥 **Interactive Selection**: Choose which episodes to download from the last 30 days
- 🎵 **Audio Download**: Extracts audio from YouTube videos (including Xiaoyuzhou Chinese podcasts)
- ⚡ **GPU-Accelerated Transcription**: Uses mlx-whisper for fast transcription on Apple Silicon
- 🗣️ **Voice-Based Speaker Diarization**: Uses pyannote.audio for accurate speaker detection (local, no API cost)
- 👥 **Speaker Identification**: Uses Claude Haiku to identify speaker names from context
- 📊 **Smart Summarization**: Generates investor-focused summaries with Claude Sonnet 4.5
- 💾 **State Management**: Tracks episode status through the entire pipeline
- 🔄 **Resumable**: Safe to interrupt and resume without re-processing
- 🌏 **Chinese Podcast Support**: Full integration with Xiaoyuzhou platform

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
2. Shows you undownloaded episodes from the last 30 days
3. You select which episodes to process (or choose "all")
4. For each episode:
   - Downloads audio
   - Transcribes with mlx-whisper (GPU-accelerated)
   - Runs voice-based speaker diarization (if configured)
   - Identifies speaker names with Claude Haiku
   - Generates summary with Claude Sonnet 4.5

### Episode Selection

When prompted, you can:
- Type `all` to process all suggested episodes
- Type `1,3,5` to process specific episodes (comma-separated)
- Type `cancel` to exit without processing

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

## Advanced Features

### Utility Scripts

- **`create_summaries_html.py`** - Compile all summaries into styled HTML for web viewing
- **`create_summaries_pdf.py`** - Generate PDF compilation of summaries via pandoc
- **`summarize_single_episode.py`** - Re-process/re-summarize individual episodes
- **`backfill_dates.py`** - Backfills publication dates for old episodes
- **`cleanup_incomplete.py`** - Removes incomplete episode folders
- **`generate_weekly_summary.py`** - Generates weekly digest of summaries
- **`summary_tester.py`** - Tests summarization on existing transcripts

### Status Tracking

The system maintains two status files:
- `podcast_status.json` - Machine-readable state
- `podcast_status.md` - Human-readable overview

### Parallel Safety

File-based locking prevents duplicate processing if you accidentally run multiple instances.

## Cost Estimates

Per episode (approximate):
- Transcription (Whisper): $0.10-0.30
- Diarization (pyannote, local): $0.00 (runs locally on your machine)
- Speaker ID (Claude Haiku, 15 min): $0.05-0.20
- Summarization (Claude Sonnet 4.5): $0.20-1.00
- **Total: ~$0.35-1.50 per episode**

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
