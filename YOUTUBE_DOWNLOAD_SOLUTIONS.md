# YouTube Download Solutions: Research Notes

**Date:** 2025-12-16
**Context:** Investigating alternatives to yt-dlp for bypassing YouTube anti-bot measures

---

## Executive Summary

**Key Finding:** ScrapingBee **CANNOT** download actual video/audio files - it only extracts metadata (titles, descriptions, captions).

**Solution:** Use `yt-dlp` + residential proxy services to avoid IP blocking while downloading at scale.

**Recommended:** Webshare ($18-22/month for 50-100 episodes)

---

## ScrapingBee: What It Actually Does

### Capabilities
- ✅ Scrapes metadata (titles, descriptions, view counts)
- ✅ Extracts YouTube captions/transcripts (text only)
- ✅ Bypasses anti-bot measures for HTML scraping
- ❌ **Cannot download video/audio files**

### Pricing
- $49-599/month (100K-2M+ credits)
- 5-75 credits per request depending on features
- Not designed for media downloads

### Verdict
**Not suitable for podcast audio downloads.** Only useful for caption extraction (like Supadata.ai).

---

## Comparison Table: Solutions for YouTube Video/Audio Downloads

| Service | Type | Actual Video Download? | Pricing (2025) | Best For | Success Rate |
|---------|------|----------------------|----------------|----------|--------------|
| **yt-dlp + Evomi** | Tool + Proxy | YES | $0.49/GB proxy | Most cost-effective | High with residential IPs |
| **yt-dlp + Webshare** ⭐ | Tool + Proxy | YES | $1.80-2.20/GB rotating residential | Budget-friendly | Excellent |
| **yt-dlp + Smartproxy/Decodo** | Tool + Proxy | YES | $8.50-12.50/GB | Mid-range reliability | Good |
| **ScrapingBee** | API | NO (metadata only) | $49-599/mo (100K-2M+ credits) | Metadata extraction only | 99.88% for metadata |
| **BrightData** | Proxy/API | YES (custom) | $499+ enterprise | Enterprise scale | 99.99% uptime |
| **Oxylabs** | Proxy/API | YES (custom) | $4-8/GB residential | Professional projects | 85.82% YouTube |
| **Apify** | Platform | YES | $5 free/mo + usage-based | Managed cloud solution | Varies by actor |
| **Zyte API** | API | YES | $1 per 14K requests @ $500 spend | API-based scraping | High |

---

## Cost Analysis for 50-100 Podcast Episodes/Month

### Assumptions
- Average episode: 1-2 hours
- Audio download: ~50-100 MB per hour (high quality)
- Total bandwidth: 5-10 GB/month for 50-100 episodes

### Option 1: yt-dlp + Evomi (CHEAPEST)
- **Cost:** $0.49/GB = **$2.45-4.90/month**
- **Setup:** Basic (yt-dlp + proxy config)
- **Reliability:** Good for light usage
- **Note:** Cheapest residential proxies, but may have occasional connection issues

### Option 2: yt-dlp + Webshare (BEST VALUE) ⭐
- **Cost:** $1.80-2.20/GB = **$9-22/month**
- **Setup:** Basic (yt-dlp + proxy config)
- **Reliability:** Excellent
- **Note:** Great balance of price and reliability, 50% off sale currently (as of Dec 2025)

### Option 3: yt-dlp Alone (FREE but risky)
- **Cost:** $0 (uses your IP)
- **Risk:** High chance of IP blocking if downloading 50-100 episodes
- **Mitigation:** Use `--sleep-interval 10` to add delays
- **Note:** Only viable if downloading very occasionally

### Option 4: BrightData (PREMIUM)
- **Cost:** $499+/month minimum
- **Not cost-effective** for 50-100 episodes
- **Only for:** Enterprise-scale operations (thousands of videos)

---

## Recommended Solution: yt-dlp + Webshare

### Why Webshare?
- Actual video/audio download capability
- $9-22/month for 50-100 episodes
- 80M+ residential IPs across 195 countries
- Rotating proxies to avoid blocks
- Free tier available (10 proxies, 1GB) for testing
- **147x cheaper** than BrightData ($499 vs $18)

### Setup Instructions

#### 1. Install yt-dlp (if not already installed)
```bash
pip install yt-dlp
```

#### 2. Sign up for Webshare
- URL: https://www.webshare.io/pricing
- Choose "Rotating Residential Proxies"
- Select 10GB plan ($18-22/month)

#### 3. Get proxy credentials
- Dashboard → Proxy → Rotating Residential
- Copy: `username:password@proxy.webshare.io:port`

#### 4. Use with yt-dlp
```bash
yt-dlp --proxy "http://username:password@proxy.webshare.io:port" \
       --sleep-interval 5 \
       --max-sleep-interval 10 \
       --format "bestaudio" \
       <YouTube_URL>
```

### Integration with podcast_summarizer.py

**Find the download section** (currently using yt-dlp) and add proxy:

```python
# Add to .env file
WEBSHARE_PROXY_URL=http://username:password@proxy.webshare.io:port

# Modify download command
import os

proxy = os.getenv('WEBSHARE_PROXY_URL')
if proxy:
    yt_dlp_cmd = [
        'yt-dlp',
        '--proxy', proxy,
        '--sleep-interval', '5',
        '--max-sleep-interval', '10',
        '--format', 'bestaudio',
        '-o', output_path,
        video_url
    ]
else:
    # Fallback to no proxy
    yt_dlp_cmd = [
        'yt-dlp',
        '--format', 'bestaudio',
        '-o', output_path,
        video_url
    ]
```

---

## Budget Alternative: yt-dlp + Evomi

**Cost:** $2.45-4.90/month for 5-10GB
**URL:** https://evomi.com/
**Trade-off:** Less reliable (occasional outages reported)
**Good for:** Non-critical projects where you can retry failed downloads

---

## Best Practices for yt-dlp + Proxies

1. **Use residential proxies** (not datacenter) - YouTube blocks datacenter IPs aggressively
2. **Rotate proxies** every 5-10 requests
3. **Add delays** between downloads (5-10 seconds)
4. **Monitor for 429 errors** and back off if encountered
5. **Keep yt-dlp updated** - YouTube changes break downloaders frequently

### Optimal yt-dlp Command
```bash
yt-dlp --proxy "http://user:pass@residential-proxy:port" \
       --sleep-interval 5 \
       --max-sleep-interval 10 \
       --format "bestaudio[ext=m4a]" \
       --output "podcast_work/%(uploader)s/%(title)s/raw_podcast.%(ext)s" \
       --cookies cookies.txt \
       <YouTube_URL>
```

---

## When to Use Proxies vs. Free yt-dlp

### Use Proxies When:
- Downloading 50+ episodes/month
- Getting 429 (Too Many Requests) errors
- IP is getting throttled/blocked
- Need guaranteed reliability

### Stick with Free yt-dlp When:
- Downloading <10 episodes/month
- No blocking issues currently
- Can tolerate occasional failures

---

## Podscan.fm Case Study Insights

From research report on Arvid Kahl's Podscan.fm architecture:

### Key Lessons
1. **Outsource adversarial complexity**: Kahl uses ScrapingBee for metadata scraping (not audio downloads)
2. **Self-host transcription**: Faster-Whisper on bare-metal GPUs (cheaper than APIs at scale)
3. **"Words per dollar" optimization**: Uses cheaper A10 GPUs instead of H100s
4. **Residential proxies critical**: Podscan routes YouTube requests through millions of residential IPs via ScrapingBee to avoid blocking

### Architecture
```
ScrapingBee (metadata + captions)
    ↓
yt-dlp + proxies (actual audio download)
    ↓
Faster-Whisper (self-hosted transcription)
    ↓
Pyannote/similar (speaker diarization)
```

**Note:** Even Podscan likely uses a separate mechanism (yt-dlp or similar) for actual audio downloads, not just ScrapingBee.

---

## Cost Comparison Summary

For **50-100 podcast episodes/month**:

| Solution | Monthly Cost | Per Episode | Notes |
|----------|-------------|-------------|-------|
| Current (yt-dlp alone) | $0 | $0 | ⚠️ Risk of blocking |
| + Evomi proxy | $2.45-4.90 | $0.05-0.10 | Budget option |
| + Webshare proxy ⭐ | $18-22 | $0.18-0.44 | **Recommended** |
| + BrightData | $499+ | $5+ | Overkill |

---

## Decision Framework

### Question: Are you experiencing YouTube download issues?

**IF NO** → Stick with free yt-dlp (current setup)
**IF YES** → Add Webshare proxies ($18-22/month)

### Signs You Need Proxies:
- ❌ Error 429 (Too Many Requests)
- ❌ Downloads timing out
- ❌ "This video is unavailable" errors
- ❌ Extremely slow download speeds (throttling)

---

## Sources

- [The Best YouTube Scrapers of 2025: Cheap & Premium - Proxyway](https://proxyway.com/best/youtube-scrapers)
- [YouTube API | ScrapingBee](https://www.scrapingbee.com/features/youtube/)
- [ScrapingBee Pricing Breakdown](https://www.firecrawl.dev/blog/scrapingbee-pricing)
- [BrightData Pricing Plans](https://brightdata.com/pricing)
- [How to Use yt-dlp with Proxies](https://www.goproxy.com/blog/yt-dlp-scarpe-videos-proxy/)
- [Scaling YouTube Video Scraping for AI with yt-dlp and Proxies](https://medium.com/@datajournal/how-to-use-yt-dlp-to-scrape-youtube-videos-with-proxies-38255a65c20d)
- [Recommended proxy for YouTube downloads with yt-dlp - GitHub](https://github.com/yt-dlp/yt-dlp/issues/8791)
- [Evomi - $0.49/GB Residential Proxies](https://evomi.com/)
- [Webshare Proxy Pricing](https://www.webshare.io/pricing)
- [Best Cheap Residential Proxies for Web Scraping in 2025](https://scrapecreators.com/blog/best-cheap-residential-proxies-for-web-scraping-in-2025)
- Podscan.fm Architecture Research Report (provided by user)

---

## ⚠️ CRITICAL: TLS Fingerprinting Fix (REQUIRED)

### The Problem
Standard Python SSL libraries generate a distinct "fingerprint" that YouTube detects as bot traffic, **even through residential proxies**. This causes "Sign in to confirm you're not a bot" errors.

### The Solution: curl_cffi Impersonation

**Required for ALL yt-dlp usage** (with or without proxies):

```bash
# Install curl_cffi support
pip install "yt-dlp[default,curl-cffi]"

# Use browser impersonation
yt-dlp --impersonate "chrome-110:windows-10" \
       --extractor-args "youtube:player_client=android" \
       <URL>
```

**Why Android API?**
- Android client API is more lenient than web client
- Less aggressive bot detection
- Better for automated downloads

### Sticky Sessions for Large Files

**Critical for 3+ hour episodes**:

If your proxy rotates IPs mid-download, YouTube returns 403 errors. Use session pinning:

```bash
# PacketStream example
yt-dlp --proxy "http://user-session-UNIQUE_ID:password@proxy.packetstream.io:31112" ...

# Evomi example (append session ID to username)
yt-dlp --proxy "http://username-session-123456:password@resi.evomi.com:3000" ...
```

---

## Implementation for Podcast Summarizer

### Changes Made to podcast_summarizer.py:

1. **Added curl_cffi impersonation** to all yt-dlp calls
2. **Added Android player client** for better success rates
3. **Added Evomi proxy support** with sticky sessions
4. **Disabled thumbnails** to save bandwidth
5. **Auto-generates unique session IDs** for large downloads

### Updated .env Configuration:

```bash
# Add these to .env
EVOMI_PROXY_USERNAME=your_username
EVOMI_PROXY_PASSWORD=your_password
```

### How It Works:

- **Without proxy credentials**: Uses impersonation only (free, works for light usage)
- **With proxy credentials**: Adds Evomi residential proxy with sticky session

---

## Cost Analysis Update (Actual Usage)

### For 50-100 Episodes/Month (Self-Hosted Transcription)

**Assumptions:**
- Average episode: 1-2 hours
- Audio bandwidth: ~60-120MB per episode
- Total: ~5-10GB/month

| Component | Cost | Notes |
|-----------|------|-------|
| **Download (Evomi)** | $2.45-4.90/mo | $0.49/GB × 5-10GB |
| **Transcription (<3hr)** | $0 | MLX-Whisper (local, free) |
| **Transcription (3+hr)** | ~$1.50/episode | OpenAI Whisper API |
| **Diarization (<3hr)** | $0 | pyannote (local, free) |
| **Diarization (3+hr)** | ~$0.30/hr | AssemblyAI |
| **Summarization** | $0.30-1.50/episode | Claude Sonnet 4.5 |

**Total Cost per Episode:**
- **Short (<3hr)**: $0.35-1.80 (mostly summarization)
- **Long (3+hr)**: $2.50-4.50 (cloud transcription + diarization)

**Monthly Total (50 episodes):** ~$17.50-90 depending on episode mix

---

## Next Steps

1. ✅ **COMPLETED**: Added curl_cffi impersonation to podcast_summarizer.py
2. ✅ **COMPLETED**: Added Evomi proxy support with sticky sessions
3. **TODO**: Install curl_cffi: `pip install "yt-dlp[default,curl-cffi]"`
4. **TODO**: Sign up for Evomi ($0.49/GB) - https://evomi.com/
5. **TODO**: Add credentials to .env file
6. **TODO**: Test with 5-10 episodes to verify blocking is eliminated

---

**Last Updated:** 2025-12-16
