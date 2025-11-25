# Podcast Summarizer System

Automated podcast downloading, transcription, and summarization system. Publishes to [teahose.com](https://teahose.com).

## Quick Start

```bash
python podcast_summarizer.py          # Main workflow: discover, select, process episodes
python generate_weekly_summary.py     # Generate weekly digest with header image
python test_daily_email.py <email>    # Test daily email digest locally
python backfill_dates.py              # Backfill missing upload_date fields
```

## Architecture

```
project_root/
├── podcast_summarizer.py          # Main script
├── podcast_urls.txt               # Podcast playlist URLs (one per line, # Name optional)
├── one_off_episodes.txt           # One-off episode URLs (auto-removed after processing)
├── podcast_status.json            # Episode tracking state
├── summarization_prompt.md        # Summary prompt template
├── .env                           # API keys (ANTHROPIC_API_KEY required)
├── xiaoyuzhou_helper.py           # Chinese podcast platform support
├── generate_weekly_summary.py     # Weekly digest generator
├── generate_weekly_header_image.py # Header image generator
├── generate_daily_email.py        # Daily email digest generator (local)
├── test_daily_email.py            # Test script for daily emails
├── vercel.json                    # Vercel cron configuration
├── app/api/cron/daily-email/      # Daily email cron endpoint
└── podcast_work/                  # Output directory
    ├── [podcast_name]/[episode_name]/
    │   ├── raw_podcast.mp3
    │   ├── transcript_raw.md      # Before speaker ID
    │   ├── transcript.md          # After speaker ID
    │   └── summary.md
    └── one off episodes/          # One-off episodes folder
```

## Processing Pipeline

**Phase 1: Discovery** - Scans `podcast_urls.txt`, fetches new episodes, updates status
**Phase 2: Selection** - Interactive menu to select episodes (`all`, `1,2,3`, or `cancel`)
**Phase 3: Processing** - 4-step pipeline per episode:

1. **Download** - Extract audio via yt-dlp → `raw_podcast.mp3`
2. **Transcribe** → `transcript_raw.md`
   - **< 3 hours**: MLX-Whisper (local GPU, free)
   - **≥ 3 hours**: OpenAI Whisper API (cloud, ~$0.36/hr) - avoids memory issues
3. **Speaker Diarization** - Adds SPEAKER_XX labels
   - **< 3 hours**: pyannote (local, free)
   - **≥ 3 hours**: AssemblyAI (cloud) - avoids memory issues
4. **Identify Speakers** - Claude Haiku maps speaker labels to names → `transcript.md`
5. **Summarize** - Claude Sonnet 4.5 (16K tokens) → `summary.md`

## Configuration

### Required: `.env`
```
ANTHROPIC_API_KEY=sk-ant-...     # Required for speaker ID + summarization
```

### Optional: `.env`
```
OPENAI_API_KEY=sk-proj-...       # For transcribing 3+ hour episodes
ASSEMBLYAI_API_KEY=...           # For diarizing 3+ hour episodes
HUGGINGFACE_TOKEN=hf_...         # For local pyannote diarization (<3 hr)
```

### Episode Status Values
- `discovered` → `downloaded` → `transcribed` → `summarized`

### Summary Format
```markdown
# [Episode Title](VIDEO_URL)

**Podcast:** Name | **Date:** Month DD, YYYY | **Participants:** Speaker 1, Speaker 2
**Region:** Western/Chinese | **Video ID:** ID | **Transcript:** [View](./transcript.md)

---
[Summary with clickable timestamps: [[00:15:30]](VIDEO_URL&t=15m20s)]
```

## Key Features

- **Free transcription** - MLX-Whisper runs locally on M1/M2/M3 Macs
- **Smart suggestions** - New podcasts: latest episode only; existing: new episodes since last download
- **Resumable** - Status saved after each step; safe to interrupt and resume
- **Chinese support** - Xiaoyuzhou platform + auto title translation
- **One-off episodes** - Add to `one_off_episodes.txt`; auto-removed after processing
- **Parallel safety** - File-based locking prevents duplicate processing

## Cost Estimates

| Component | Cost |
|-----------|------|
| MLX-Whisper transcription (<3hr) | $0.00 (local) |
| OpenAI Whisper API (≥3hr) | ~$0.36/hr (~$1.50 for 4hr episode) |
| pyannote diarization (<3hr) | $0.00 (local) |
| AssemblyAI diarization (≥3hr) | ~$0.30/hr |
| Speaker ID (Haiku) | $0.05-0.20 |
| Summarization (Sonnet 4.5) | $0.30-1.50 |
| **Total per episode (<3hr)** | **~$0.35-1.75** |
| **Total per episode (≥3hr)** | **~$2.50-4.50** |
| Weekly summary + header image | ~$0.54-2.08 |

## Web Publishing (teahose.com)

- Auto-deploys on `git push`
- Newsletter signups via Vercel KV (see `VERCEL_KV_SETUP.md`)
- SEO: Dynamic sitemap, JSON-LD schemas, SSG for all pages
- Files: `app/sitemap.ts`, `app/robots.ts`, `lib/schema.ts`

## Daily Email Digest

Automatic daily emails sent to newsletter subscribers at 6 AM EST (only if new episodes exist).

### How It Works
- **Vercel Cron** triggers `/api/cron/daily-email` daily at 6 AM EST
- Checks for episodes uploaded in the last 24 hours
- If episodes exist, generates pithy descriptions using Claude Sonnet
- Creates header image using Gemini (Nano Banana Pro)
- Sends HTML email via SendGrid to all Vercel KV subscribers
- Email includes: header image, episode cards with title, podcast, participants, and description

### Required Environment Variables (Vercel)
```
SENDGRID_API_KEY=SG.xxx           # SendGrid API key
ANTHROPIC_API_KEY=sk-ant-xxx      # For generating descriptions
GOOGLE_API_KEY=xxx                # For header image generation
CRON_SECRET=xxx                   # Optional: secure cron endpoint
```

### Testing Locally
```bash
python test_daily_email.py altmbr@gmail.com   # Send test email
```

### Manual Trigger
Visit `https://teahose.com/api/cron/daily-email` to trigger manually.

## Dependencies

```
mlx-whisper anthropic python-dotenv pyannote.audio yt-dlp openai assemblyai
```
System: `ffmpeg`, `python3.8+`, Apple Silicon recommended

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ANTHROPIC_API_KEY not set` | Add to `.env` |
| `mlx-whisper not found` | `pip install mlx-whisper` |
| `yt-dlp not found` | `pip install yt-dlp` or `brew install yt-dlp` |
| `ffmpeg not found` | `brew install ffmpeg` |
| Script hangs | Waiting for input in Phase 2; Ctrl+C to cancel |
| Duplicate downloads | Delete stale `processing.lock` |

## Customization

- **Summary format**: Edit `summarization_prompt.md`
- **Whisper model**: Change `WHISPER_MODEL` in `podcast_summarizer.py` (tiny/base/small/medium/large)
- **Summary length**: Modify `max_tokens` in `summarize_transcript_with_ai()` (default: 16000)
