"""Audio download using yt-dlp."""
import subprocess
import os
import shutil
from pathlib import Path


# Firefox User-Agent to match cookies (required for Cloudflare bypass)
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0"

# Cookie file path (mounted from GCP Secret Manager - READ-ONLY)
COOKIE_FILE_SOURCE = "/secrets/YOUTUBE_COOKIES"

# Writable copy in /tmp (yt-dlp needs to write to cookie file)
COOKIE_FILE_WRITABLE = "/tmp/youtube-cookies.txt"


def download_audio(video_url: str, output_path: Path) -> Path:
    """
    Download audio from YouTube video using yt-dlp.

    Args:
        video_url: YouTube video URL
        output_path: Path to save audio file

    Returns:
        Path to downloaded audio file
    """
    print(f"Downloading audio from: {video_url}")

    # Copy cookie file from read-only secret mount to writable /tmp
    if os.path.exists(COOKIE_FILE_SOURCE):
        cookie_size = os.path.getsize(COOKIE_FILE_SOURCE)
        print(f"✓ Cookie file found: {COOKIE_FILE_SOURCE} ({cookie_size} bytes)")
        print(f"  Copying to writable location: {COOKIE_FILE_WRITABLE}")
        shutil.copy2(COOKIE_FILE_SOURCE, COOKIE_FILE_WRITABLE)
        # Make it writable
        os.chmod(COOKIE_FILE_WRITABLE, 0o644)
        print(f"✓ Cookie file ready at {COOKIE_FILE_WRITABLE}")
    else:
        print(f"✗ Cookie file NOT FOUND: {COOKIE_FILE_SOURCE}")
        print(f"  Contents of /secrets: {os.listdir('/secrets') if os.path.exists('/secrets') else 'DIR NOT FOUND'}")
        raise RuntimeError(f"Cookie file not found at {COOKIE_FILE_SOURCE}")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Download audio with yt-dlp
    cmd = [
        "yt-dlp",
        "-x",  # Extract audio
        "--audio-format", "mp3",
        "--audio-quality", "0",  # Best quality
        "--verbose",  # Verbose output for debugging
        "--js-runtimes", "node",  # Use Node.js for JavaScript challenges
        "--cookies", COOKIE_FILE_WRITABLE,  # Use writable cookie file
        "--user-agent", USER_AGENT,  # Match browser User-Agent (critical for Cloudflare)
        "--extractor-args", "youtube:player_client=web",  # Use web client
        "-o", str(output_path),
        video_url
    ]

    print(f"Running command: {' '.join(cmd[:8])}...")  # Print first part of command
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Print stdout for debugging
    if result.stdout:
        print(f"yt-dlp stdout:\n{result.stdout[-2000:]}")  # Last 2000 chars

    if result.returncode != 0:
        print(f"yt-dlp stderr:\n{result.stderr[-2000:]}")  # Last 2000 chars
        raise RuntimeError(f"yt-dlp failed: {result.stderr}")

    print(f"✓ Audio downloaded to: {output_path}")
    return output_path
