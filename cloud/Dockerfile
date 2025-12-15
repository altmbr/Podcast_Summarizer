# Dockerfile for Podcast Processor
# Optimized with layer caching: dependencies cached separately from code
# CPU version (GPU support commented out, ready to enable when quota approved)

FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# ============================================================================
# LAYER 1: System dependencies (rarely changes - good cache layer)
# ============================================================================
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    nodejs \
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
# LAYER 3: Application code (changes frequently - invalidates only this layer)
# ============================================================================
# Copy code LAST so that code changes don't invalidate dependency layers above
COPY processor/ ./processor/

# Entry point
ENTRYPOINT ["python3", "-m", "processor.main"]
