"""Audio download using yt-dlp."""
import subprocess
from pathlib import Path


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

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Download audio with yt-dlp
    cmd = [
        "yt-dlp",
        "-x",  # Extract audio
        "--audio-format", "mp3",
        "--audio-quality", "0",  # Best quality
        "-o", str(output_path),
        video_url
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp failed: {result.stderr}")

    print(f"✓ Audio downloaded to: {output_path}")
    return output_path
