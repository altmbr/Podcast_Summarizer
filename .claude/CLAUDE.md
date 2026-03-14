# Podcast Summarizer System

Automated podcast downloading, transcription, and summarization system. Publishes to [teahose.com](https://www.teahose.com).

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
├── podcast_summarizer.py          # Main script (local pipeline)
├── podcast_urls.txt               # Podcast playlist URLs (one per line, # Name optional)
├── one_off_episodes.txt           # One-off episode URLs (auto-removed after processing)
├── podcast_config.json            # Podcast metadata + Podscan ID mappings
├── podcast_status.json            # Episode tracking state (old pipeline)
├── podscan_status.json            # Episode tracking state (Podscan pipeline)
├── summarization_prompt.md        # Summary prompt template
├── .env                           # API keys (PODSCAN_API_KEY, etc.)
├── xiaoyuzhou_helper.py           # Chinese podcast platform support
├── generate_weekly_summary.py     # Weekly digest generator
├── generate_weekly_header_image.py # Header image generator
├── generate_daily_email.py        # Daily email digest generator (local)
├── test_daily_email.py            # Test script for daily emails
├── vercel.json                    # Vercel cron configuration
├── app/api/cron/daily-email/      # Daily email cron endpoint
├── cloud/
│   ├── functions/
│   │   ├── podscan_processor/     # ★ Primary pipeline: Podscan → Claude → Git
│   │   ├── discovery/             # Old: YouTube episode discovery
│   │   └── webhook/               # Old: email reply webhook
│   ├── processor/                 # Old: Cloud Run Job (Whisper + pyannote)
│   └── scripts/
│       ├── deploy_all.sh          # GCP deployment script
│       └── lookup_podscan_ids.py  # Helper to find Podscan podcast IDs
└── podcast_work/                  # Output directory
    └── [podcast_name]/[episode_name]/
        ├── transcript.md          # Speaker-labeled transcript
        └── summary.md             # AI-generated summary
```

## Processing Pipelines

### Primary: Podscan Pipeline (automated, GCP Cloud Function)

Fully automated. Runs daily at 8 PM EST via Cloud Scheduler.

**Flow:** Cloud Scheduler → `podscan-processor` Cloud Function → git push → Vercel auto-deploys

1. **Discover** — Poll Podscan API for new episodes (last 3 days) across 20 mapped podcasts
2. **Fetch transcript** — Podscan provides timestamped, speaker-labeled transcripts
3. **Speaker names** — Replace SPEAKER_XX labels with real names from Podscan metadata (no LLM needed)
4. **Summarize** — Claude Sonnet (16K tokens) → `summary.md`
5. **Publish** — Git commit + push → Vercel auto-deploys to teahose.com

**Cost:** ~$0.30/episode (Claude summarization only)

**GCP resources:**
- Cloud Function: `podscan-processor` (Gen 2, 512MB, 60-min timeout)
- Cloud Scheduler: `podscan-daily` (8 PM EST daily)
- Secrets: `PODSCAN_API_KEY`, `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `SENDGRID_API_KEY`, `GOOGLE_API_KEY`
- Service account: `podcast-processor@gen-lang-client-0111593271.iam.gserviceaccount.com`

**Podscan API:**
- Base URL: `https://podscan.fm/api/v1`
- Auth: Bearer token in Authorization header
- Key endpoints: `/podcasts/{id}/episodes`, `/episodes/{id}`, `/podcasts/search`
- Rate limits: daily limit (returns 429 with `daily_limit_exceeded`), courtesy 2s delay between requests
- Transcript field: `episode_transcript`
- Speaker info: `metadata.hosts[].speaker_label`, `metadata.guests[].speaker_label`

### Legacy: Local Pipeline (manual, Apple Silicon Mac)

Still available for YouTube-only feeds and one-off episodes.

1. **Download** — yt-dlp → `raw_podcast.mp3`
2. **Transcribe** — MLX-Whisper (local, free) or OpenAI Whisper API (3hr+)
3. **Diarize** — pyannote (local) or AssemblyAI (3hr+)
4. **Speaker ID** — Claude Haiku
5. **Summarize** — Claude Sonnet → `summary.md`

## Podcast Config (`podcast_config.json`)

Maps podcast names to hosts and Podscan IDs. 20 of 25 podcasts have Podscan IDs.

**Not on Podscan** (need legacy pipeline or manual processing):
- More or Less, Stanford AI Speaker Series, Theory Ventures Office Hours, Zhang Xiaoyun's

Podscan IDs were sourced from the Panasonic project (`/Documents/Panasonic/newsletter-pipeline/src/types.ts` and `Vibing/podcasts/download_transcripts.py`).

## Configuration

### `.env`
```
PODSCAN_API_KEY=...              # For Podscan transcript fetching
```

### GCP Secrets (for Cloud Function)
```
ANTHROPIC_API_KEY                # Claude summarization
GITHUB_TOKEN                     # Git push (PAT with repo scope)
SENDGRID_API_KEY                 # Processing report emails
PODSCAN_API_KEY                  # Transcript fetching
GOOGLE_API_KEY                   # Gemini (future use)
```

### Vercel Environment Variables (for daily email)
```
SENDGRID_API_KEY                 # Email sending
ANTHROPIC_API_KEY                # Episode descriptions
GOOGLE_API_KEY                   # Header image generation (Gemini)
CRON_SECRET                      # Secure cron endpoint
```

## Web Publishing (teahose.com)

- Auto-deploys on `git push` via Vercel
- Newsletter signups via Vercel KV (see `VERCEL_KV_SETUP.md`)
- **SEO optimized**: Dynamic sitemap, JSON-LD schemas, SSG for all pages, canonical URLs
- Base URL: `https://www.teahose.com` (with www for SEO consistency)

## Daily Email Digest

Automatic daily emails sent to newsletter subscribers at 6 AM EST (only if new episodes exist).

- **Vercel Cron** triggers `/api/cron/daily-email` daily at 6 AM EST
- Generates pithy descriptions using Claude Sonnet
- Creates header image using Gemini (`gemini-3-pro-image-preview`)
- Sends HTML email via SendGrid to all Vercel KV subscribers

### Testing Locally
```bash
python test_daily_email.py altmbr@gmail.com   # Send test email
```

## GCP Deployment

```bash
cd cloud && bash scripts/deploy_all.sh
```

Steps 1-5: Legacy pipeline (Docker image, Cloud Run Job, Discovery, Webhook, Scheduler)
Steps 6-7: Podscan pipeline (Cloud Function, Scheduler)

**Manual trigger:**
```bash
curl 'https://us-central1-gen-lang-client-0111593271.cloudfunctions.net/podscan-processor?dry_run=true'
```

**Check logs:**
```bash
gcloud functions logs read podscan-processor --region us-central1 --project gen-lang-client-0111593271 --limit 30
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Podscan daily limit exceeded | Wait 24h for reset; check with `curl` |
| GitHub token expired | Generate new PAT at github.com/settings/tokens, update GCP secret |
| Function import errors | Check `__pycache__` isn't in deploy source; redeploy |
| No episodes processed | Check `podscan_status.json` and `LOOKBACK_DAYS` env var |
| Summary format wrong | Verify `summary.md` header matches `lib/schema.ts` parser |

## Customization

- **Summary format**: Edit `summarization_prompt.md`
- **Whisper model**: Change `WHISPER_MODEL` in `podcast_summarizer.py` (tiny/base/small/medium/large)
- **Summary length**: Modify `max_tokens` in summarize functions (default: 16000)
- **Lookback window**: Set `LOOKBACK_DAYS` env var (default: 3)
