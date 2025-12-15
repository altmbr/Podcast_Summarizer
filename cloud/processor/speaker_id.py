"""Speaker identification using Claude Haiku."""
import re
from anthropic import Anthropic


def identify_speakers(transcript_raw: str, episode_title: str, anthropic_api_key: str) -> str:
    """
    Identify speakers in transcript using Claude Haiku.

    Args:
        transcript_raw: Transcript with SPEAKER_XX labels
        episode_title: Episode title for context
        anthropic_api_key: Anthropic API key

    Returns:
        Transcript with real speaker names
    """
    print("Identifying speakers with Claude Haiku...")

    client = Anthropic(api_key=anthropic_api_key)

    # Extract unique speaker labels
    speaker_labels = set(re.findall(r'SPEAKER_\d+', transcript_raw))
    print(f"Found {len(speaker_labels)} unique speakers: {sorted(speaker_labels)}")

    # Build prompt
    prompt = f"""You are analyzing a podcast transcript. The transcript has speaker labels like SPEAKER_00, SPEAKER_01, etc.

Episode title: {episode_title}

Here is a sample of the transcript (first 3000 characters):
{transcript_raw[:3000]}

Based on the content, context, and episode title, identify who each speaker is. Provide a mapping in this exact format:

SPEAKER_00: [Name and role]
SPEAKER_01: [Name and role]

Be specific but concise. If you can't determine a name, describe their role (e.g., "Host", "Guest", "Interviewer").
"""

    response = client.messages.create(
        model="claude-haiku-4-20250414",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    mapping_text = response.content[0].text
    print(f"Claude's speaker mapping:\n{mapping_text}")

    # Parse mapping
    speaker_map = {}
    for line in mapping_text.split('\n'):
        match = re.match(r'(SPEAKER_\d+):\s*(.+)', line)
        if match:
            speaker_map[match.group(1)] = match.group(2).strip()

    # Apply mapping to transcript
    result = transcript_raw
    for old_label, new_name in speaker_map.items():
        result = result.replace(f"{old_label}:", f"{new_name}:")

    print(f"✓ Speaker identification complete")
    return result
