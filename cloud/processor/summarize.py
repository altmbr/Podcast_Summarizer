"""Transcript summarization using Claude Sonnet."""
from pathlib import Path
from anthropic import Anthropic


def summarize_transcript(
    transcript: str,
    episode_title: str,
    podcast_name: str,
    video_url: str,
    upload_date: str,
    anthropic_api_key: str
) -> str:
    """
    Summarize transcript using Claude Sonnet.

    Args:
        transcript: Full transcript with speaker names
        episode_title: Episode title
        podcast_name: Podcast name
        video_url: Video URL
        upload_date: Upload date (YYYYMMDD format)
        anthropic_api_key: Anthropic API key

    Returns:
        Formatted summary in markdown
    """
    print("Summarizing with Claude Sonnet...")

    client = Anthropic(api_key=anthropic_api_key)

    # Load summarization prompt template
    # For now, use a basic prompt (we can customize later)
    prompt = f"""Summarize this podcast transcript. Create a comprehensive summary with:

1. Key themes and main topics discussed
2. Notable quotes or insights
3. Any contrarian or surprising perspectives
4. Practical takeaways or action items

Episode: {episode_title}
Podcast: {podcast_name}

Transcript:
{transcript[:100000]}  # Limit to fit in context

Format the summary in markdown with clear sections and bullet points."""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt}]
    )

    summary_content = response.content[0].text

    # Format with metadata header
    date_formatted = format_date(upload_date)

    header = f"""# [{episode_title}]({video_url})

**Podcast:** {podcast_name} | **Date:** {date_formatted}
**Video URL:** {video_url} | **Transcript:** [View](./transcript.md)

---

"""

    result = header + summary_content

    print(f"✓ Summary generated ({len(summary_content)} characters)")
    return result


def format_date(date_str: str) -> str:
    """Format YYYYMMDD to readable date."""
    if not date_str or len(date_str) != 8:
        return "Unknown"
    try:
        year = date_str[:4]
        month = date_str[4:6]
        day = date_str[6:8]
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        month_name = months[int(month) - 1]
        return f"{month_name} {int(day)}, {year}"
    except:
        return date_str
