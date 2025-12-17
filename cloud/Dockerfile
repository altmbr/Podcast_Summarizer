# Dockerfile for Podcast Processor
# Optimized with layer caching: dependencies cached separately from code
# CPU version (GPU support commented out, ready to enable when quota approved)

FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# ============================================================================
# LAYER 1: System dependencies (rarely changes - good cache layer)
# ============================================================================
# Install curl_cffi dependencies for browser impersonation
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    nodejs \
    libcurl4-openssl-dev \
    libssl-dev \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ============================================================================
# LAYER 2: Python dependencies (changes only when requirements.txt changes)
# ============================================================================
# Copy ONLY requirements.txt first (not the entire codebase)
# This ensures pip install layer is cached unless requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================================================================
# LAYER 2.5: Pre-download ML models (saves ~10 min per job execution)
# ============================================================================
# faster-whisper large-v3 model (~3GB) - downloads once at build time
# Without this, Cloud Run downloads fresh on every job (ephemeral filesystem)
ENV HF_HOME=/app/models
RUN python3 -c "from faster_whisper import WhisperModel; WhisperModel('large-v3', device='cpu', compute_type='int8')"

# ============================================================================
# LAYER 3: Application code (changes frequently - invalidates only this layer)
# ============================================================================
# Copy code LAST so that code changes don't invalidate dependency layers above
COPY processor/ ./processor/

# Entry point
ENTRYPOINT ["python3", "-m", "processor.main"]
