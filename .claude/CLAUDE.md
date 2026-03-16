# Teahose — Podcast & Newsletter Summarizer

Automated podcast and newsletter summarization system. Publishes to [teahose.com](https://www.teahose.com).

## Quick Start

```bash
python podcast_summarizer.py          # Main workflow: discover, select, process episodes
python test_daily_email.py <email>    # Test daily email digest locally
python backfill_dates.py              # Backfill missing upload_date fields
```

## Architecture

```
project_root/
├── podcast_summarizer.py          # Main script (local pipeline)
├── podcast_urls.txt               # Podcast playlist URLs (one per line, # Name optional)
├── one_off_episodes.txt           # One-off episode URLs (auto-removed after processing)
├── podcast_config.json            # Podcast metadata + Podscan IDs + YouTube playlist IDs
├── newsletter_config.json         # Newsletter sender → name/author mappings
├── podcast_status.json            # Episode tracking state (old pipeline)
├── podscan_status.json            # Episode tracking state (Podscan pipeline)
├── newsletter_status.json         # Newsletter tracking state
├── .env                           # API keys (local dev)
├── test_daily_email.py            # Test script for daily emails
├── vercel.json                    # Vercel cron configuration
├── app/api/cron/daily-email/      # Daily email cron endpoint (Vercel)
├── cloud/
│   ├── email-worker/              # ★ Cloudflare Email Worker (newsletter ingestion)
│   │   ├── src/index.ts           # Email handler: parse, filter, forward to GCP
│   │   └── wrangler.toml          # Cloudflare Worker config
│   ├── functions/
│   │   ├── podscan_processor/     # ★ Podcast pipeline: Podscan → Claude → Git
│   │   ├── newsletter_processor/  # ★ Newsletter pipeline: Email → Claude → Git
│   │   ├── discovery/             # Old: YouTube episode discovery
│   │   └── webhook/               # Old: email reply webhook
│   └── scripts/
│       ├── deploy_all.sh          # GCP deployment script
│       └── lookup_podscan_ids.py  # Helper to find Podscan podcast IDs
└── podcast_work/                  # Output directory (podcasts AND newsletters)
    └── [source_name]/[episode_or_issue_title]/
        ├── transcript.md          # Speaker-labeled transcript (podcasts only)
        └── summary.md             # AI-generated summary
```

## Processing Pipelines

### 1. Podcast Pipeline (automated, GCP Cloud Function)

Fully automated. Runs 3x daily at **10 AM, 3 PM, 10 PM EST** via Cloud Scheduler.

**Flow:** Cloud Scheduler → `podscan-processor` Cloud Function → git push → Vercel auto-deploys

1. **Discover** — Poll Podscan API for new episodes (last 3 days) across 20 mapped podcasts
2. **Fetch transcript** — Podscan provides timestamped, speaker-labeled transcripts
3. **Speaker names** — Replace SPEAKER_XX labels with real names from Podscan metadata
4. **YouTube lookup** — Match episode to YouTube video via playlist ID + search API fallback
5. **Summarize** — Claude Sonnet 4.6 (16K tokens) → `summary.md` with clickable YouTube timestamps
6. **Publish** — Git commit + push → Vercel auto-deploys to teahose.com

**Cost:** ~$0.30/episode (Claude summarization only)

**YouTube timestamps:** Timestamps like `[00:19:18]` become clickable links to the exact moment on YouTube. Lookup uses playlist scan first, then YouTube search API scoped to the channel as fallback.

### 2. Newsletter Pipeline (automated, Cloudflare Email Worker + GCP Cloud Function)

Fully automated. Processes newsletters in real-time as they arrive.

**Flow:** Email → Cloudflare Email Worker → `newsletter-processor` Cloud Function → git push → Vercel auto-deploys

1. **Receive** — Email arrives at `newsletters@teahose.com`
2. **Filter** — Cloudflare Worker detects transactional emails (confirmations, welcome, verification) and forwards those to `altmbr@gmail.com`. Real newsletters go to the processor.
3. **Extract** — BeautifulSoup + html2text strips HTML chrome, tracking pixels, footers
4. **Summarize** — Claude Sonnet 4.6 → `summary.md` with `**Source:** newsletter` metadata
5. **Publish** — Git commit + push → Vercel auto-deploys

**Transactional email filter patterns:** confirm, verif, activate, subscribe, opt-in, welcome, thank you, thanks for, on the list, getting started, verification code. Also forwards emails < 500 chars.

**Adding new newsletters:** Subscribe with `newsletters@teahose.com`. Confirmation emails auto-forward to Gmail. Add sender to `newsletter_config.json` for proper naming.

### 3. Legacy Pipeline (manual, Apple Silicon Mac)

Still available for YouTube-only feeds and one-off episodes.

## Podcast Config (`podcast_config.json`)

Maps podcast names to hosts, Podscan IDs, and YouTube playlist IDs. 20 of 25 podcasts have Podscan IDs.

**Not on Podscan** (need legacy pipeline):
- More or Less, Stanford AI Speaker Series, Theory Ventures Office Hours, Zhang Xiaoyun's

## Newsletter Config (`newsletter_config.json`)

Maps sender email addresses to newsletter names and authors. Currently tracking:
- Stratechery, StrictlyVC, 99d, Newcomer Newsletter, Sourcery Newsletter, The VC Corner, PitchBook, Data Driven VC

## Configuration

### `.env` (local development)
```
PODSCAN_API_KEY=...              # Podscan transcript fetching
ANTHROPIC_API_KEY=...            # Claude summarization + descriptions
GOOGLE_API_KEY=...               # Gemini header images + YouTube Data API
AWS_ACCESS_KEY_ID=...            # AWS SES email sending
AWS_SECRET_ACCESS_KEY=...        # AWS SES email sending
```

### GCP Secrets (for Cloud Functions)
```
ANTHROPIC_API_KEY                # Claude summarization
GITHUB_TOKEN                     # Git push (classic PAT with repo scope)
AWS_ACCESS_KEY_ID                # AWS SES email sending
AWS_SECRET_ACCESS_KEY            # AWS SES email sending
PODSCAN_API_KEY                  # Transcript fetching
GOOGLE_API_KEY                   # Gemini + YouTube Data API
NEWSLETTER_WEBHOOK_SECRET        # HMAC auth for newsletter webhook
```

### Vercel Environment Variables (for daily email + KV)
```
AWS_ACCESS_KEY_ID                # AWS SES email sending
AWS_SECRET_ACCESS_KEY            # AWS SES email sending
ANTHROPIC_API_KEY                # Episode descriptions + chat
GOOGLE_API_KEY                   # Header image generation (Gemini)
CRON_SECRET                      # Secure cron endpoint
EMAILS_KV_REST_API_URL           # Vercel KV (subscriber storage) — auto-set by Vercel
EMAILS_KV_REST_API_TOKEN         # Vercel KV — auto-set by Vercel
```

**KV Notes:**
- Subscriber list stored in Vercel KV (Upstash Redis). KV client configured in `lib/kv.ts` using `EMAILS_` prefixed env vars.
- Free-tier KV databases auto-delete after 14 days of inactivity. If this happens, create a new KV in Vercel dashboard, restore from Upstash backups, and Vercel will auto-set the env vars.
- Admin endpoint: `GET /api/admin/subscribers` returns current subscriber list.
- Manual daily email trigger: `curl "https://www.teahose.com/api/cron/daily-email?hours=48"` (all subscribers) or add `?test=true` for just altmbr@gmail.com.

### Cloudflare (Email Worker)
- **Worker:** `newsletter-email-worker` (deployed via `wrangler deploy` from `cloud/email-worker/`)
- **Secret:** `WEBHOOK_SECRET` (set via `wrangler secret put WEBHOOK_SECRET`)
- **Routing:** `newsletters@teahose.com` → Send to Worker
- **Routing:** `agent@teahose.com` → Forward to `altmbr@gmail.com`

### AWS (SES email sending)
- **Region:** us-west-2 (Oregon)
- **IAM user:** `ses-sender` (AmazonSESFullAccess policy)
- **Verified domain:** teahose.com (DKIM via Cloudflare DNS)
- **Sends from:** `agent@teahose.com` (daily email), `podscan@teahose.com` (processing reports), `newsletter@teahose.com` (newsletter reports)
- **Cost:** ~$0.10 per 1,000 emails (was $20/month on SendGrid)

## Infrastructure & Domains

### Domain: teahose.com
- **Registrar:** GoDaddy
- **DNS:** Cloudflare (nameservers: `casey.ns.cloudflare.com`, `aida.ns.cloudflare.com`)
- **Email routing:** Cloudflare Email Routing (MX records point to Cloudflare)
- **DKIM:** 3 CNAME records for AWS SES (in Cloudflare, proxy OFF)

### Hosting & Services
| Service | Provider | Purpose |
|---------|----------|---------|
| Website | Vercel | Next.js app, auto-deploys on git push |
| Subscriber list | Vercel KV | Newsletter email storage |
| Podcast processing | GCP Cloud Functions | Podscan → Claude → git push |
| Newsletter processing | GCP Cloud Functions | Email → Claude → git push |
| Email ingestion | Cloudflare Email Workers | Receive newsletters, filter, forward to GCP |
| Email sending | AWS SES (us-west-2) | Daily digest + processing reports |
| Secrets (GCP) | GCP Secret Manager | API keys for Cloud Functions |
| Backup | GCS | Git bundles if push fails |

### GCP Resources
- Cloud Function: `podscan-processor` (Gen 2, 512MB, 60-min timeout)
- Cloud Function: `newsletter-processor` (Gen 2, 512MB, 5-min timeout)
- Cloud Scheduler: `podscan-daily` (10 AM, 3 PM, 10 PM EST)
- GCS bucket: `gen-lang-client-0111593271-podscan-backups`
- Service account: `podcast-processor@gen-lang-client-0111593271.iam.gserviceaccount.com`

### GitHub
- **Repo:** `altmbr/Podcast_Summarizer` (private)
- **Auth:** Classic PAT with `repo` scope, stored in GCP secret `GITHUB_TOKEN`

## Web Publishing (teahose.com)

- Auto-deploys on `git push` via Vercel
- **Homepage tabs:** Recent Content (all), Podcasts (sources), Newsletters (sources)
- Newsletter signups via Vercel KV (see `VERCEL_KV_SETUP.md`)
- **SEO optimized**: Dynamic sitemap, JSON-LD schemas, SSG for all pages, canonical URLs
- Base URL: `https://www.teahose.com` (with www for SEO consistency)

## Daily Email Digest

Automatic daily emails sent to newsletter subscribers at 6 AM EST (only if new content exists).

- **Vercel Cron** triggers `/api/cron/daily-email` daily at 6 AM EST
- Generates pithy descriptions using Claude Sonnet
- Creates header image using Gemini (`gemini-3-pro-image-preview`)
- Sends HTML email via AWS SES to all Vercel KV subscribers
- Includes both podcast episodes and newsletter summaries

### Testing Locally
```bash
python test_daily_email.py altmbr@gmail.com   # Send test email
python test_daily_email.py altmbr@gmail.com 3 # Look back 3 days
```

## Deployment

### Podcast/Newsletter Cloud Functions
```bash
cd cloud && bash scripts/deploy_all.sh
```

### Cloudflare Email Worker
```bash
cd cloud/email-worker && npx wrangler deploy
```

### Manual triggers
```bash
# Podcast processor
curl 'https://us-central1-gen-lang-client-0111593271.cloudfunctions.net/podscan-processor'

# Dry run (no git push)
curl 'https://us-central1-gen-lang-client-0111593271.cloudfunctions.net/podscan-processor?dry_run=true'
```

### Check logs
```bash
# Podcast processor
gcloud functions logs read podscan-processor --region us-central1 --project gen-lang-client-0111593271 --limit 30

# Newsletter processor
gcloud functions logs read newsletter-processor --region us-central1 --project gen-lang-client-0111593271 --limit 30
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Podscan daily limit exceeded | Wait 24h for reset; check with `curl` |
| GitHub token expired | Generate new classic PAT (repo scope) at github.com/settings/tokens, update GCP secret |
| Git push fails | Summaries auto-backed up to GCS bucket; re-run after fixing token |
| AWS SES sandbox | Request production access in SES console; sandbox only sends to verified emails |
| No episodes processed | Check `podscan_status.json` and `LOOKBACK_DAYS` env var |
| Summary format wrong | Verify `summary.md` header matches `lib/schema.ts` parser |
| Junk newsletter processed | Add pattern to transactional filter in `cloud/email-worker/src/index.ts`, delete from `podcast_work/`, redeploy worker |
| Newsletter not showing in tab | Check `newsletter_config.json` has the sender, summary has `**Source:** newsletter` |
| YouTube timestamps not linking | Check `podcast_config.json` has `youtube_playlist` for that podcast, verify YouTube Data API enabled on Google API key |

## Customization

- **Summary format**: Edit `SUMMARIZATION_PROMPT` in `cloud/functions/podscan_processor/main.py`
- **Newsletter summary format**: Edit `NEWSLETTER_SUMMARIZATION_PROMPT` in `cloud/functions/newsletter_processor/main.py`
- **Summary length**: Modify `max_tokens` in summarize functions (default: 16000)
- **Lookback window**: Set `LOOKBACK_DAYS` env var (default: 3)
- **Podcast schedule**: Update Cloud Scheduler `podscan-daily` cron expression
- **Transactional email filter**: Edit regex in `cloud/email-worker/src/index.ts`
