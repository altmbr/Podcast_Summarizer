"""Speaker diarization using Pyannote."""
from pathlib import Path
from typing import List, Dict
from pyannote.audio import Pipeline
import torch


def diarize_audio(audio_path: Path, hf_token: str) -> List[Dict]:
    """
    Perform speaker diarization using Pyannote.

    Args:
        audio_path: Path to audio file
        hf_token: Hugging Face token for pyannote model access

    Returns:
        List of speaker segments with start, end, and speaker label
    """
    print("Diarizing with Pyannote...")

    # Load pipeline
    # Use CPU for now (device=torch.device("cpu"))
    # Will use CUDA when GPU quota approved
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        token=hf_token
    )

    # Force CPU usage
    pipeline.to(torch.device("cpu"))

    # Run diarization
    diarization = pipeline(str(audio_path))

    # Convert to list of segments
    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "start": turn.start,
            "end": turn.end,
            "speaker": speaker
        })

    print(f"✓ Diarization complete: {len(segments)} speaker segments, {len(set(s['speaker'] for s in segments))} unique speakers")
    return segments
