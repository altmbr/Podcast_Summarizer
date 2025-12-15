"""Audio transcription using Faster-Whisper."""
from pathlib import Path
from typing import List, Dict
from faster_whisper import WhisperModel


def transcribe_audio(audio_path: Path, model_size: str = "large-v3") -> List[Dict]:
    """
    Transcribe audio using Faster-Whisper.

    Args:
        audio_path: Path to audio file
        model_size: Whisper model size (tiny, base, small, medium, large-v3)

    Returns:
        List of segments with start, end, and text
    """
    print(f"Transcribing with Faster-Whisper ({model_size})...")

    # Load model (CPU for now, will use GPU when available)
    # device="cpu" for CPU, device="cuda" for GPU
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # Transcribe
    segments, info = model.transcribe(
        str(audio_path),
        beam_size=5,
        language="en"  # Set to None for auto-detection
    )

    print(f"Detected language: {info.language} (probability: {info.language_probability:.2f})")
    print(f"Duration: {info.duration:.2f} seconds")

    # Convert segments to list
    result = []
    for segment in segments:
        result.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    print(f"✓ Transcription complete: {len(result)} segments")
    return result
