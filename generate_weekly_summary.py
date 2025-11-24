#!/usr/bin/env python3
"""
Generate a weekly summary from all podcast episodes published in the last week.
Filters by upload_date (when the podcast was published), not discovered_date.
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import image generation functions
from generate_weekly_header_image import extract_themes_from_summary, generate_header_image, format_date_string

# Configuration
PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_WORK_DIR = Path("./podcast_work")
WEEKLY_SUMMARY_PROMPT_FILE = Path("./weekly_summary prompt.md")
WEEKLY_SUMMARIES_DIR = Path("./weekly_summaries")
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"

# Default prompt if file doesn't exist or is empty
DEFAULT_WEEKLY_PROMPT = """You are analyzing podcast summaries from the past week to create a comprehensive weekly digest for investors and entrepreneurs.

Review all the podcast summaries provided below and synthesize them into a cohesive weekly summary that includes:

## 1. Key Themes Across All Episodes (5-10 themes)
- Identify the major themes that emerged across multiple podcasts this week
- Group related insights together
- Highlight any contrarian or surprising viewpoints

## 2. Top Insights (10-15 insights)
- Select the most valuable insights across all episodes
- Focus on actionable takeaways
- Include speaker attribution where important

## 3. Notable Quotes (5-10 quotes)
- Pick the most impactful quotes across all episodes
- Include speaker name and podcast source

## 4. Companies & People Mentioned (5-15 entries)
- List notable companies discussed across episodes
- Include people who were frequently referenced or featured
- Note why they were mentioned (excellence, innovation, case studies, etc.)

## 5. Operating Insights (3-7 insights)
- Tactical takeaways for business operations
- Decision-making frameworks discussed
- Best practices shared

Format the output in clear markdown with headers, bullet points, and emphasis where appropriate.
Focus on synthesizing across episodes rather than summarizing each individually.
"""

def load_podcast_status():
    """Load podcast status from JSON file"""
    if not PODCAST_STATUS_FILE.exists():
        print(f"❌ Error: {PODCAST_STATUS_FILE} not found")
        sys.exit(1)

    with open(PODCAST_STATUS_FILE, 'r') as f:
        return json.load(f)

def load_weekly_prompt():
    """Load the weekly summary prompt from file or use default"""
    if WEEKLY_SUMMARY_PROMPT_FILE.exists():
        content = WEEKLY_SUMMARY_PROMPT_FILE.read_text().strip()
        if content:
            return content

    print(f"⚠ Note: Using default weekly summary prompt")
    print(f"   You can customize by editing: {WEEKLY_SUMMARY_PROMPT_FILE}")
    return DEFAULT_WEEKLY_PROMPT

def get_episodes_from_last_week(status_data, days=7, debug=False):
    """
    Get all episodes published in the last N days with status = summarized.
    Returns list of dicts with episode metadata and file paths.
    """
    # Set cutoff to start of day (N+1) days ago, then use > comparison
    # This ensures episodes from N days ago are included
    cutoff_date = (datetime.now() - timedelta(days=days + 1)).replace(hour=0, minute=0, second=0, microsecond=0)
    episodes = []

    if debug:
        print(f"   Cutoff date: {cutoff_date}")

    for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
        podcast_name = podcast_data.get("podcast_name", "Unknown")

        # Skip if podcast name is None or empty
        if not podcast_name or podcast_name == "None":
            continue

        # Skip one-off episodes (they shouldn't be included in weekly summaries)
        if podcast_name == "One-off Episodes":
            continue

        for video_id, episode_data in podcast_data.get("episodes", {}).items():
            # Only include summarized episodes
            if episode_data.get("status") != "summarized":
                continue

            # Check upload_date (published date)
            upload_date = episode_data.get("upload_date")
            if not upload_date or len(upload_date) != 8:
                continue

            try:
                episode_date = datetime.strptime(upload_date, '%Y%m%d')
                if episode_date >= cutoff_date:
                    episode_title = episode_data.get("title", "Unknown")

                    if debug:
                        print(f"   Checking: [{podcast_name}] {episode_title[:50]}")

                    # Find the actual summary file by searching the podcast folder
                    podcast_folder = PODCAST_WORK_DIR / podcast_name
                    summary_path = None

                    if podcast_folder.exists():
                        # Search for any summary.md file in subdirectories
                        # Match by checking if the video_id is in the summary file header
                        for episode_folder in podcast_folder.iterdir():
                            if episode_folder.is_dir():
                                potential_summary = episode_folder / "summary.md"
                                if potential_summary.exists():
                                    # Read first 500 chars to check for video ID
                                    try:
                                        with open(potential_summary, 'r', encoding='utf-8') as f:
                                            header = f.read(500)
                                        if video_id in header:
                                            summary_path = potential_summary
                                            if debug:
                                                print(f"      ✓ Found summary")
                                            break
                                    except Exception as e:
                                        continue
                    else:
                        if debug:
                            print(f"      ✗ Podcast folder doesn't exist: {podcast_folder}")

                    if summary_path and summary_path.exists():
                        episodes.append({
                            "podcast_name": podcast_name,
                            "title": episode_title,
                            "video_id": video_id,
                            "upload_date": upload_date,
                            "upload_date_formatted": f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}",
                            "summary_path": summary_path,
                            "episode_date": episode_date
                        })
                    else:
                        if debug:
                            print(f"      ✗ Summary not found (path={summary_path})")
            except ValueError:
                continue

    # Sort by upload date (newest first)
    episodes.sort(key=lambda x: x["episode_date"], reverse=True)
    return episodes

def sanitize_filename(filename):
    """Sanitize a string to be used as a valid filename"""
    import re
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = filename.strip('. ')
    return filename

def get_teahose_url(podcast_name, episode_slug):
    """Generate teahose.com URL for an episode"""
    from urllib.parse import quote
    encoded_podcast = quote(podcast_name)
    encoded_slug = quote(episode_slug)
    return f"https://teahose.com/podcast/{encoded_podcast}/{encoded_slug}"

def read_summary_file(summary_path):
    """Read a summary file and return its content"""
    try:
        with open(summary_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"  ⚠ Error reading {summary_path}: {e}")
        return ""

def generate_weekly_summary_with_ai(episodes, weekly_prompt):
    """Generate a weekly summary using Claude"""
    print(f"  → Generating weekly summary with AI...")

    try:
        from anthropic import Anthropic
    except ImportError:
        print("❌ Error: Anthropic SDK not installed")
        print("   Install with: pip install anthropic")
        sys.exit(1)

    anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        print("❌ Error: ANTHROPIC_API_KEY not set in .env file")
        sys.exit(1)

    # Build episode URL mapping for teahose.com
    episode_urls = []
    for ep in episodes:
        # Extract episode slug from the summary path (parent folder name)
        episode_slug = ep["summary_path"].parent.name
        teahose_url = get_teahose_url(ep["podcast_name"], episode_slug)
        episode_urls.append(f'- **{ep["title"]}** → {teahose_url}')

    # Insert episode URLs into the prompt
    episode_urls_section = "\n".join(episode_urls)
    weekly_prompt_with_urls = weekly_prompt.replace(
        "[Episode URLs will be automatically injected here by the script]",
        episode_urls_section
    )

    # Build the combined content from all episode summaries
    combined_summaries = []
    for ep in episodes:
        summary_content = read_summary_file(ep["summary_path"])
        if summary_content:
            combined_summaries.append(f"""
---
**Podcast:** {ep['podcast_name']}
**Episode:** {ep['title']}
**Published:** {ep['upload_date_formatted']}
---

{summary_content}
""")

    if not combined_summaries:
        print("❌ No summaries found to process")
        return None

    # Combine all summaries with the prompt
    all_content = "\n\n".join(combined_summaries)
    full_prompt = f"""{weekly_prompt_with_urls}

---

# PODCAST SUMMARIES FROM THIS WEEK

{all_content}
"""

    # Call Claude API
    client = Anthropic(api_key=anthropic_api_key)

    print(f"  → Sending {len(combined_summaries)} episode summaries to Claude...")
    print(f"  → Total input size: {len(full_prompt):,} characters")

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=16000,  # Increased from 8000 to handle 20+ episodes comprehensively
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    summary_text = response.content[0].text
    print(f"  ✓ Weekly summary generated ({len(summary_text):,} characters)")
    return summary_text

def save_weekly_summary(summary_text, episodes, days=7):
    """Save the weekly summary to a file with header image"""
    WEEKLY_SUMMARIES_DIR.mkdir(exist_ok=True)

    # Generate filename based on date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    filename = f"weekly_summary_{start_date.strftime('%Y-%m-%d')}_to_{end_date.strftime('%Y-%m-%d')}.md"
    output_path = WEEKLY_SUMMARIES_DIR / filename

    # First, save a temporary version to extract themes from
    temp_content = f"""# Weekly Podcast Summary

**Period:** {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}
**Episodes Analyzed:** {len(episodes)}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Episodes Included

"""
    for ep in episodes:
        episode_slug = ep["summary_path"].parent.name
        teahose_url = get_teahose_url(ep["podcast_name"], episode_slug)
        temp_content += f"- **{ep['podcast_name']}** - [{ep['title']}]({teahose_url}) ({ep['upload_date_formatted']})\n"

    temp_content += "\n---\n\n" + summary_text

    # Save temporary version for theme extraction
    with open(output_path, 'w') as f:
        f.write(temp_content)

    # Generate header image
    print("→ Generating header image...")
    try:
        # Extract themes from the summary
        panel_titles = extract_themes_from_summary(str(output_path))

        if panel_titles:
            # Generate image filename
            image_filename = f"weekly_summary_{start_date.strftime('%Y-%m-%d')}_to_{end_date.strftime('%Y-%m-%d')}_header.png"
            image_path = WEEKLY_SUMMARIES_DIR / image_filename

            # Format date for header
            date_str = format_date_string(f"{start_date.strftime('%Y-%m-%d')}_to_{end_date.strftime('%Y-%m-%d')}")

            # Generate the image
            generate_header_image(panel_titles, date_str, str(image_path))

            # Now rebuild the file with the image at the top
            with open(output_path, 'w') as f:
                f.write(f"![Podcast Weekly Digest Header](./{image_filename})\n\n")
                f.write(f"# Weekly Podcast Summary\n\n")
                f.write(f"**Period:** {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}\n")
                f.write(f"**Episodes Analyzed:** {len(episodes)}\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                # List episodes included
                f.write("## Episodes Included\n\n")
                for ep in episodes:
                    episode_slug = ep["summary_path"].parent.name
                    teahose_url = get_teahose_url(ep["podcast_name"], episode_slug)
                    f.write(f"- **{ep['podcast_name']}** - [{ep['title']}]({teahose_url}) ({ep['upload_date_formatted']})\n")

                f.write("\n---\n\n")
                f.write(summary_text)

            print(f"  ✓ Header image saved to: {image_path}")
        else:
            print("  ⚠ Could not extract themes, skipping header image")

    except Exception as e:
        print(f"  ⚠ Header image generation failed: {e}")
        print("  Continuing without header image...")
        # Keep the temp content (already saved without image)

    # Also generate HTML version for email
    print("→ Generating HTML version for email...")
    html_filename = f"weekly_summary_{start_date.strftime('%Y-%m-%d')}_to_{end_date.strftime('%Y-%m-%d')}.html"
    html_output_path = WEEKLY_SUMMARIES_DIR / html_filename

    # Convert markdown to HTML
    generate_html_version(output_path, html_output_path, episodes, start_date, end_date, image_filename if panel_titles else None)
    print(f"  ✓ HTML version saved to: {html_output_path}")

    return output_path

def generate_html_version(md_path, html_path, episodes, start_date, end_date, image_filename=None):
    """Generate an HTML version of the weekly summary for email"""
    import markdown

    # Read the markdown content
    with open(md_path, 'r') as f:
        content = f.read()

    # Extract just the summary content (after the episodes list and separator)
    # Note: Full weekly summary has 2 separators (header, Claude's header, content)
    # Pithy summary has 1 separator (header, content)
    # We want everything after the LAST separator
    parts = content.split('\n---\n')
    if len(parts) >= 2:
        # Take everything after the LAST separator
        # For full summary with 2 separators: parts[2] onwards
        # For pithy summary with 1 separator: parts[1] onwards
        # Check if parts[1] starts with "**A." to determine if it's the main content
        if len(parts) > 2 and not parts[1].strip().startswith('**'):
            # Full summary: skip duplicate header in parts[1], use parts[2] onwards
            summary_content = '\n---\n'.join(parts[2:]).strip()
        else:
            # Pithy summary or unknown: use everything after first separator
            summary_content = '\n---\n'.join(parts[1:]).strip()
    else:
        summary_content = content

    # Convert markdown to HTML using markdown library
    # Note: We'll do some preprocessing to handle the nested structure better
    import re

    # The markdown library struggles with the format:
    # 1. **Topic**
    # - quote
    # So we'll preprocess to make quotes into blockquotes or paragraphs

    # Replace bullet points under numbered items with proper indentation
    lines = summary_content.split('\n')
    processed_lines = []
    in_numbered_list = False

    for i, line in enumerate(lines):
        # Check if this is a numbered list item with bold topic
        if re.match(r'^\d+\.\s+\*\*', line):
            in_numbered_list = True
            processed_lines.append(line)
        # Check if this is ANY bullet point under a numbered item (quotes, descriptions, etc.)
        elif in_numbered_list and line.strip().startswith('- '):
            # Convert to indented paragraph instead of list item
            processed_lines.append('    ' + line.strip()[2:])  # Remove "- " and indent
        else:
            processed_lines.append(line)
            # Reset if we hit a blank line or section header
            if not line.strip() or line.startswith('**'):
                in_numbered_list = False

    processed_content = '\n'.join(processed_lines)

    md_converter = markdown.Markdown(extensions=['extra', 'nl2br'])
    summary_html = md_converter.convert(processed_content)

    # Replace "link" with "Read Summary" in all citation links (old format)
    summary_html = re.sub(r'>\s*link\s*</a>', '>Read Summary</a>', summary_html)

    # Convert plain teahose.com URLs to "Read Summary" links (new format)
    # Pattern: (Podcast, Speaker, https://teahose.com/...)
    summary_html = re.sub(
        r'\(([^,]+),\s*([^,]+),\s*(https://teahose\.com/[^)]+)\)',
        r'(\1, \2, <a href="\3">Read Summary</a>)',
        summary_html
    )

    # Build episodes list HTML from markdown (extract from parts[0])
    episodes_html = ""
    episode_count = 0
    if len(parts) >= 1:
        # Extract episodes from the first part (our header section)
        header_part = parts[0]
        # Find the Episodes Included section
        episodes_match = re.search(r'## Episodes Included\n\n(.*)', header_part, re.DOTALL)
        if episodes_match:
            episodes_md = episodes_match.group(1).strip()
            # Convert each line to HTML
            for line in episodes_md.split('\n'):
                if line.strip().startswith('- **'):
                    # Extract podcast name, title with link, and date
                    match = re.match(r'- \*\*([^*]+)\*\* - \[([^\]]+)\]\(([^)]+)\) \(([^)]+)\)', line)
                    if match:
                        podcast_name, title, url, date = match.groups()
                        episodes_html += f'<li><strong>{podcast_name}</strong> - <a href="{url}">{title}</a> ({date})</li>\n'
                        episode_count += 1

    # Build complete HTML
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; color: #333; }}
        h1 {{ color: #1a1a1a; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; }}
        h2 {{ color: #2c2c2c; margin-top: 30px; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        ul {{ padding-left: 20px; }}
        li {{ margin: 8px 0; }}
        strong {{ color: #1a1a1a; }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .meta {{ color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="header">
        {"<img src='./" + image_filename + "' style='max-width: 100%; height: auto;' />" if image_filename else ""}
        <h1>Weekly Podcast Summary</h1>
        <p class="meta"><strong>Period:</strong> {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}<br>
        <strong>Episodes Analyzed:</strong> {episode_count}</p>
    </div>

    <h2>Episodes Included</h2>
    <ul>
{episodes_html}
    </ul>

    <hr style="margin: 40px 0; border: none; border-top: 2px solid #e0e0e0;">

{summary_html}
</body>
</html>
"""

    # Save HTML
    with open(html_path, 'w') as f:
        f.write(html)

def main():
    print(f"\n{'='*70}")
    print(f"📊 WEEKLY PODCAST SUMMARY GENERATOR")
    print(f"{'='*70}\n")

    # Load podcast status
    print("→ Loading podcast status...")
    status_data = load_podcast_status()
    print("  ✓ Status loaded")

    # Load weekly prompt
    print("→ Loading weekly summary prompt...")
    weekly_prompt = load_weekly_prompt()
    print("  ✓ Prompt loaded")

    # Get episodes from last week
    print("\n→ Finding episodes from the last 7 days...")
    import sys
    debug = '--debug' in sys.argv
    if debug:
        print(f"   Debug mode enabled")
    episodes = get_episodes_from_last_week(status_data, days=7, debug=debug)

    if not episodes:
        print("\n❌ No summarized episodes found from the last 7 days")
        print("   Episodes must:")
        print("   - Have been published (upload_date) in the last 7 days")
        print("   - Have status = 'summarized'")
        print("   - Have a summary.md file")
        sys.exit(0)

    print(f"  ✓ Found {len(episodes)} episode(s)\n")

    # Display episodes
    print("Episodes to include:")
    for i, ep in enumerate(episodes, 1):
        print(f"  {i}. [{ep['podcast_name']}] {ep['title']}")
        print(f"     Published: {ep['upload_date_formatted']}")

    print(f"\n{'='*70}")
    print("Generating weekly summary...")
    print(f"{'='*70}\n")

    # Generate summary
    summary_text = generate_weekly_summary_with_ai(episodes, weekly_prompt)

    if not summary_text:
        print("❌ Failed to generate summary")
        sys.exit(1)

    # Save summary
    print("\n→ Saving weekly summary...")
    output_path = save_weekly_summary(summary_text, episodes)

    print(f"\n{'='*70}")
    print(f"✅ WEEKLY SUMMARY COMPLETE")
    print(f"{'='*70}")
    print(f"\n📄 Summary saved to: {output_path}")
    print(f"   Episodes analyzed: {len(episodes)}")
    print(f"   Output size: {len(summary_text):,} characters\n")

if __name__ == "__main__":
    main()
