# Future Improvements for Cloud Podcast Processor

## Performance Optimizations

### 1. Bake faster-whisper model into Docker image
**Priority:** High
**Impact:** ~5-10 minute reduction per job execution

Currently, the `large-v3` model (~3GB) downloads fresh on every Cloud Run job execution because the filesystem is ephemeral.

**Solution:** Pre-download the model during Docker build by adding to Dockerfile:

```dockerfile
# Download faster-whisper model during build (add after pip install)
RUN python3 -c "from faster_whisper import WhisperModel; WhisperModel('large-v3', device='cpu', compute_type='int8', download_root='/app/models')"
ENV HF_HOME=/app/models
```

**Trade-offs:**
- Docker image size increases by ~3GB (from ~2GB to ~5GB)
- Build time increases by ~5-10 minutes (one-time cost)
- Runtime startup becomes instant (saves 5-10 min per execution)
- Artifact Registry storage cost increases slightly (~$0.10/month for 3GB)

**When to implement:** Before processing multiple episodes regularly. The time savings compound quickly - processing 10 episodes saves ~50-100 minutes of model download time.

---

## Other Potential Optimizations

### 2. Persistent disk for models (alternative to baking)
Use Cloud Run volumes with GCS FUSE to cache models between runs. More complex but allows dynamic model switching.

### 3. Smaller model for shorter episodes
Switch to `base` or `small` model for episodes < 30 minutes if accuracy requirements are flexible.

### 4. Use OpenAI Whisper API for very long episodes
For 3+ hour episodes, OpenAI API (~$0.36/hr) might be faster than downloading + running large-v3 locally.
