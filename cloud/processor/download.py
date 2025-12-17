"""Audio download using yt-dlp."""
import subprocess
import os
import shutil
from pathlib import Path


# Optional cookie file path (mounted from GCP Secret Manager - READ-ONLY)
COOKIE_FILE_SOURCE = "/secrets/YOUTUBE_COOKIES"
COOKIE_FILE_WRITABLE = "/tmp/youtube-cookies.txt"


def download_audio(video_url: str, output_path: Path) -> Path:
    """
    Download audio from YouTube video using yt-dlp.

    Uses Evomi residential proxy + curl_cffi impersonation to bypass blocking.
    Cookies are optional - only used if the secret is mounted.

    Args:
        video_url: YouTube video URL
        output_path: Path to save audio file

    Returns:
        Path to downloaded audio file
    """
    print(f"Downloading audio from: {video_url}")

    # Check for optional cookie file
    use_cookies = False
    if os.path.exists(COOKIE_FILE_SOURCE):
        cookie_size = os.path.getsize(COOKIE_FILE_SOURCE)
        print(f"✓ Cookie file found: {COOKIE_FILE_SOURCE} ({cookie_size} bytes)")
        shutil.copy2(COOKIE_FILE_SOURCE, COOKIE_FILE_WRITABLE)
        os.chmod(COOKIE_FILE_WRITABLE, 0o644)
        use_cookies = True
    else:
        print("ℹ No cookie file - using proxy + impersonation only")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Download audio with yt-dlp
    cmd = [
        "yt-dlp",
        "-x",  # Extract audio
        "--audio-format", "mp3",
        "--audio-quality", "0",  # Best quality
        "--verbose",  # Verbose output for debugging
        "--no-write-thumbnail",  # Save bandwidth
        "--impersonate", "chrome-110:windows-10",  # CRITICAL: Bypass TLS fingerprinting
        "--extractor-args", "youtube:player_client=android",  # Android client is more lenient
        "-o", str(output_path),
    ]

    # Add cookies if available
    if use_cookies:
        cmd.extend(["--cookies", COOKIE_FILE_WRITABLE])

    # Add Evomi residential proxy if configured (from GCP environment variables)
    evomi_username = os.getenv("EVOMI_PROXY_USERNAME")
    evomi_password = os.getenv("EVOMI_PROXY_PASSWORD")

    if evomi_username and evomi_password:
        # Use sticky session (same IP for entire download - critical for large files)
        # Note: Make sure "Sticky Session" is selected in Evomi dashboard, NOT "Rotating"
        proxy_url = f"http://{evomi_username}:{evomi_password}@core-residential.evomi.com:1000"
        cmd.extend(["--proxy", proxy_url])
        print(f"✓ Using Evomi residential proxy (sticky session enabled)")
    else:
        print("⚠ Evomi proxy credentials not found - running without proxy (may get blocked)")

    cmd.append(video_url)

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
