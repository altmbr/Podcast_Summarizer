"""Merge transcription segments with speaker diarization."""
from typing import List, Dict


def merge_transcript_with_diarization(
    transcript_segments: List[Dict],
    diarization_segments: List[Dict]
) -> str:
    """
    Merge transcription with diarization to create labeled transcript.

    Args:
        transcript_segments: List of transcription segments (start, end, text)
        diarization_segments: List of diarization segments (start, end, speaker)

    Returns:
        Formatted transcript with speaker labels
    """
    print("Merging transcript with diarization...")

    # Build speaker map for each transcript segment
    transcript_with_speakers = []

    for trans_seg in transcript_segments:
        trans_start = trans_seg["start"]
        trans_end = trans_seg["end"]
        trans_mid = (trans_start + trans_end) / 2

        # Find overlapping speaker
        speaker = "SPEAKER_00"  # Default
        max_overlap = 0

        for diar_seg in diarization_segments:
            diar_start = diar_seg["start"]
            diar_end = diar_seg["end"]

            # Calculate overlap
            overlap_start = max(trans_start, diar_start)
            overlap_end = min(trans_end, diar_end)
            overlap = max(0, overlap_end - overlap_start)

            if overlap > max_overlap:
                max_overlap = overlap
                speaker = diar_seg["speaker"]

        transcript_with_speakers.append({
            "start": trans_start,
            "end": trans_end,
            "speaker": speaker,
            "text": trans_seg["text"]
        })

    # Format as markdown
    lines = []
    current_speaker = None

    for seg in transcript_with_speakers:
        timestamp = format_timestamp(seg["start"])
        speaker = seg["speaker"]
        text = seg["text"]

        # Add speaker label if changed
        if speaker != current_speaker:
            if current_speaker is not None:
                lines.append("")  # Blank line between speakers
            current_speaker = speaker

        lines.append(f"[{timestamp}] {speaker}: {text}")

    result = "\n".join(lines)
    print(f"✓ Merged transcript: {len(lines)} lines")
    return result


def format_timestamp(seconds: float) -> str:
    """Format seconds as [HH:MM:SS]."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"
