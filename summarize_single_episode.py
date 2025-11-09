#!/usr/bin/env python3
"""
Quick script to generate summary for a single episode that already has a transcript.
"""

import os
import sys
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

def load_summarization_prompt():
    """Load the custom summarization prompt from file."""
    prompt_file = "summarization_prompt.md"
    if os.path.exists(prompt_file):
        with open(prompt_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    else:
        raise FileNotFoundError(f"Summarization prompt file not found: {prompt_file}")

def summarize_transcript_with_ai(transcript_text, video_title, custom_prompt, participants_list=None):
    """
    Use Claude Sonnet 4.5 to summarize the podcast transcript.

    Args:
        transcript_text: The full transcript text
        video_title: The title of the video/episode
        custom_prompt: The customization prompt from summarization_prompt.md
        participants_list: Optional list of participant names
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not set in .env file")

    client = Anthropic(api_key=api_key)

    # Build the prompt
    user_message = f"""Here is a podcast transcript to summarize:

Title: {video_title}

Transcript:
{transcript_text}

---

{custom_prompt}

Please provide a comprehensive summary following the format specified above."""

    print(f"\n📊 Generating summary with Claude Sonnet 4.5...")
    print(f"   Transcript length: {len(transcript_text):,} characters")

    # Call Claude API
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=16000,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": user_message
        }]
    )

    summary = response.content[0].text

    # Count tokens for cost estimation
    input_tokens = response.usage.input_tokens
    output_tokens = response.usage.output_tokens

    # Cost calculation (approximate, based on current pricing)
    input_cost = (input_tokens / 1_000_000) * 3.00  # $3 per million input tokens
    output_cost = (output_tokens / 1_000_000) * 15.00  # $15 per million output tokens
    total_cost = input_cost + output_cost

    print(f"   Input tokens: {input_tokens:,}")
    print(f"   Output tokens: {output_tokens:,}")
    print(f"   Estimated cost: ${total_cost:.4f}")

    return summary

def extract_metadata_from_transcript(transcript_path):
    """Extract metadata from the transcript header."""
    metadata = {}
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[:20]:  # Check first 20 lines for metadata
            if line.startswith('**Title:**'):
                metadata['title'] = line.replace('**Title:**', '').strip()
            elif line.startswith('**Podcast:**'):
                metadata['podcast'] = line.replace('**Podcast:**', '').strip()
            elif line.startswith('**Date:**'):
                metadata['date'] = line.replace('**Date:**', '').strip()
            elif line.startswith('**URL:**'):
                metadata['url'] = line.replace('**URL:**', '').strip()
            elif line.startswith('**Participants:**'):
                metadata['participants'] = line.replace('**Participants:**', '').strip()
    return metadata

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize_single_episode.py <path_to_transcript.md>")
        sys.exit(1)

    transcript_path = sys.argv[1]

    if not os.path.exists(transcript_path):
        print(f"Error: Transcript file not found: {transcript_path}")
        sys.exit(1)

    # Determine output path (same directory, summary.md)
    episode_dir = os.path.dirname(transcript_path)
    summary_path = os.path.join(episode_dir, "summary.md")

    print(f"\n🎯 Summarizing episode...")
    print(f"   Transcript: {transcript_path}")
    print(f"   Summary will be saved to: {summary_path}")

    # Load the transcript
    print(f"\n📖 Reading transcript...")
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript_text = f.read()

    # Extract metadata
    metadata = extract_metadata_from_transcript(transcript_path)
    video_title = metadata.get('title', 'Unknown Episode')

    # Load summarization prompt
    custom_prompt = load_summarization_prompt()

    # Generate summary
    summary = summarize_transcript_with_ai(transcript_text, video_title, custom_prompt)

    # Prepare the summary with metadata header
    summary_with_metadata = f"""**Title:** {metadata.get('title', 'Unknown')}
**Podcast:** {metadata.get('podcast', 'Unknown')}
**Date:** {metadata.get('date', 'Unknown')}
**Participants:** {metadata.get('participants', 'Unknown')}
**URL:** {metadata.get('url', 'Unknown')}
**Transcript:** [transcript.md](transcript.md)

---

{summary}
"""

    # Save the summary
    print(f"\n💾 Saving summary to: {summary_path}")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_with_metadata)

    print(f"\n✅ Summary generated successfully!")
    print(f"   Location: {summary_path}")

if __name__ == "__main__":
    main()
