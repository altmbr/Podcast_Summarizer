#!/usr/bin/env python3
"""
Generate a daily email digest with all episodes from the last 24 hours.
Creates HTML email with episode cards, descriptions, and header image.
"""

import os
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_WORK_DIR = Path("./podcast_work")
DAILY_EMAILS_DIR = Path("./daily_emails")
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"
CLAUDE_HAIKU_MODEL = "claude-haiku-4-20250414"  # Cheaper model for short descriptions
OPENAI_IMAGE_MODEL = "gpt-image-1"

def load_podcast_status():
    """Load podcast status from JSON file"""
    if not PODCAST_STATUS_FILE.exists():
        print(f"❌ Error: {PODCAST_STATUS_FILE} not found")
        sys.exit(1)

    with open(PODCAST_STATUS_FILE, 'r') as f:
        return json.load(f)

def get_episodes_from_last_day(status_data):
    """
    Get all episodes published in the last 24 hours with status = summarized.
    Returns list of dicts with episode metadata and file paths.
    """
    cutoff_date = datetime.now() - timedelta(days=1)
    episodes = []

    for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
        podcast_name = podcast_data.get("podcast_name", "Unknown")

        if not podcast_name or podcast_name == "None":
            continue

        # Skip one-off episodes
        if podcast_name == "One-off Episodes":
            continue

        for video_id, episode_data in podcast_data.get("episodes", {}).items():
            # Only include summarized episodes
            if episode_data.get("status") != "summarized":
                continue

            # Check upload_date (YYYYMMDD format)
            upload_date_str = episode_data.get("upload_date")
            if not upload_date_str or upload_date_str == "0":
                continue

            try:
                upload_date = datetime.strptime(upload_date_str, "%Y%m%d")
            except ValueError:
                continue

            # Only include episodes from last 24 hours
            if upload_date < cutoff_date:
                continue

            # Build file paths
            title = episode_data.get("title", "Unknown")
            sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)

            episode_folder = PODCAST_WORK_DIR / podcast_name / sanitized_title
            summary_file = episode_folder / "summary.md"

            if not summary_file.exists():
                continue

            episodes.append({
                "podcast_name": podcast_name,
                "title": title,
                "video_id": video_id,
                "upload_date": upload_date,
                "summary_path": summary_file,
                "video_url": f"https://www.youtube.com/watch?v={video_id}",
                "region": episode_data.get("region", "Western")
            })

    # Sort by upload_date (newest first)
    episodes.sort(key=lambda x: x["upload_date"], reverse=True)
    return episodes

def extract_key_themes_from_summary(summary_path):
    """Extract content for AI to summarize - returns summary text, not final description"""
    try:
        with open(summary_path, 'r') as f:
            content = f.read()

        # Find the Key Themes section
        themes_match = re.search(r'##?\s*(?:1\.|A\.)\s*Key\s+Themes.*?\n(.*?)(?=\n##\s*\d|\n##\s*[A-Z]|\Z)', content, re.DOTALL | re.IGNORECASE)

        if themes_match:
            return themes_match.group(1).strip()[:2000]  # Return first 2000 chars of themes

        # Fallback to full summary (truncated)
        return content[:2000]

    except Exception as e:
        print(f"⚠ Warning: Could not read summary from {summary_path}: {e}")
        return None

def generate_episode_descriptions(episodes):
    """Generate pithy 1-2 sentence descriptions using Claude Haiku (cost-efficient)"""
    from anthropic import Anthropic

    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    descriptions = {}

    for episode in episodes:
        # Extract key themes from summary (NOT transcript) for efficiency
        summary_excerpt = extract_key_themes_from_summary(episode['summary_path'])

        if not summary_excerpt:
            descriptions[episode['video_id']] = "New episode available."
            continue

        # Use Sonnet for high-quality pithy descriptions
        prompt = f"""Write ONE pithy sentence (max 15 words) capturing the most interesting insight from this podcast episode. Be specific, punchy, intriguing.

Episode: {episode['title']}

Key themes:
{summary_excerpt}

One sentence:"""

        try:
            response = client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=100,
                messages=[{"role": "user", "content": prompt}]
            )
            descriptions[episode['video_id']] = response.content[0].text.strip()
        except Exception as e:
            print(f"⚠ Warning: Could not generate description for {episode['title']}: {e}")
            descriptions[episode['video_id']] = "New episode available."

    return descriptions

def generate_header_image(episodes, date_str, output_path):
    """Generate a header image showing today's topics using Google Nano Banana Pro"""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("⚠ Installing google-genai...")
        import subprocess
        subprocess.run(["pip", "install", "-q", "google-genai"], check=True)
        from google import genai
        from google.genai import types

    if not episodes:
        return None

    # Extract topics from episode titles (use actual count, max 6)
    topics = []
    for ep in episodes[:6]:
        title = ep['title']
        # Remove common prefixes
        title = re.sub(r'^.*?:\s*', '', title)
        # Take first part if there's a pipe or dash
        title = re.split(r'\s*[\|\-]\s*', title)[0]
        # Shorten if too long
        if len(title) > 50:
            title = title[:47] + "..."
        topics.append(title)

    num_topics = len(topics)

    # Determine grid layout based on number of topics
    if num_topics == 1:
        layout = "1 large panel filling the entire image"
        panel_desc = f'Single Panel: "{topics[0]}"'
    elif num_topics == 2:
        layout = "2 panels side by side (1 row × 2 columns)"
        panel_desc = f'Panel 1 (left): "{topics[0]}"\nPanel 2 (right): "{topics[1]}"'
    elif num_topics == 3:
        layout = "3 panels (1 large on left, 2 stacked on right)"
        panel_desc = f'Panel 1 (left, tall): "{topics[0]}"\nPanel 2 (top-right): "{topics[1]}"\nPanel 3 (bottom-right): "{topics[2]}"'
    elif num_topics == 4:
        layout = "4 panels in a 2×2 grid"
        panel_desc = f'Panel 1 (top-left): "{topics[0]}"\nPanel 2 (top-right): "{topics[1]}"\nPanel 3 (bottom-left): "{topics[2]}"\nPanel 4 (bottom-right): "{topics[3]}"'
    elif num_topics == 5:
        layout = "5 panels: 2 on top row, 3 on bottom row"
        panel_desc = f'Panel 1 (top-left): "{topics[0]}"\nPanel 2 (top-right): "{topics[1]}"\nPanel 3 (bottom-left): "{topics[2]}"\nPanel 4 (bottom-center): "{topics[3]}"\nPanel 5 (bottom-right): "{topics[4]}"'
    else:  # 6
        layout = "6 panels in a 3×2 grid (3 rows × 2 columns)"
        panel_desc = f'Panel 1 (top-left): "{topics[0]}"\nPanel 2 (top-right): "{topics[1]}"\nPanel 3 (middle-left): "{topics[2]}"\nPanel 4 (middle-right): "{topics[3]}"\nPanel 5 (bottom-left): "{topics[4]}"\nPanel 6 (bottom-right): "{topics[5]}"'

    # Create image prompt optimized for Nano Banana Pro (great at text rendering)
    prompt = f"""Create a vintage 1950s newspaper-style comic header for a daily podcast digest.

LAYOUT: {layout} in LANDSCAPE format (wider than tall).

STYLE: Vintage 1950s Roy Lichtenstein pop art aesthetic with these specific characteristics:
- BACKGROUND: Warm aged cream paper (#f7f4f0) with subtle halftone dot texture
- BORDERS: Thick black outlines (3px) around all panels
- COLORS: Bold pop art accents - cardinal red (#c41e3a), golden yellow (#f4c430), deep blue (#2d5a7b)
- SHADOWS: Black comic drop shadows (not brown)
- TEXTURE: Ben Day halftone dots for shading, stipple patterns
- OVERALL: Clean vintage newspaper comic with warm base + bold accent colors

PANEL CONTENT (each panel must have):
- Visual metaphor representing the topic (characters, objects, symbols)
- Bold sans-serif UPPERCASE text labels
- Each panel uses one bold accent color (rotate red/yellow/blue)
- Thick black panel borders
- 1950s comic book character style with halftone shading

TOPICS FOR {num_topics} PANELS:
{panel_desc}

FOOTER BANNER: Bold black text "THE DAILY TEAHOSE - {date_str}" on cream background strip

REQUIREMENTS:
- All {num_topics} panels clearly visible and equal-sized
- Warm cream aged paper background throughout
- Bold red/yellow/blue accents only (no orange, no bright green)
- All text UPPERCASE and highly legible
- Landscape orientation
- Professional vintage newspaper comic quality"""

    try:
        google_api_key = os.environ.get("GOOGLE_API_KEY")
        if not google_api_key:
            print("⚠ Warning: GOOGLE_API_KEY not set - cannot generate header image")
            return None

        client = genai.Client(api_key=google_api_key)

        # Use Nano Banana Pro (gemini-3-pro-image-preview)
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        # Extract and save the generated image
        for part in response.parts:
            if part.inline_data is not None:
                # Save the image
                image = part.as_image()
                image.save(str(output_path))
                print(f"✓ Header image generated with Nano Banana Pro: {output_path}")
                return output_path

        print("⚠ Warning: No image data in response")
        return None

    except Exception as e:
        print(f"⚠ Warning: Could not generate header image with Nano Banana Pro: {e}")
        return None

def generate_html_email(episodes, descriptions, header_image_path, date_str):
    """Generate HTML email content using table-based layout for cross-client compatibility"""
    import base64
    import urllib.parse
    from PIL import Image
    from io import BytesIO

    # EMAIL HTML BEST PRACTICES (2025):
    # - Tables for ALL layout (email clients use Word rendering, not browser)
    # - 600px max width (fits email preview panes)
    # - 100% inline CSS (Gmail strips <style> tags)
    # - No box-shadow (fails in Outlook, some Gmail configs)
    # - No display: inline-block (breaks on email forward)
    # - Use <div> not <p> inside <td> (Gmail can break <p> out of cells)
    # - Double-declare: bgcolor attribute + background-color style
    # - Use full hex codes (#ffffff not #fff)

    # Color palette - using full hex codes (no shorthand) for max compatibility
    colors = {
        'background': '#f7f4f0',      # Warm aged cream paper
        'foreground': '#1a1a1a',      # True black text
        'card': '#fffefa',            # Warm white cards
        'muted_foreground': '#555555', # Secondary text
        'accent': '#c41e3a',          # Cardinal red
        'border': '#1a1a1a',          # Black borders
    }

    # Compress and convert image to base64 for email embedding
    header_img_html = ""
    if header_image_path and header_image_path.exists():
        try:
            # Open and compress the image
            img = Image.open(header_image_path)

            # Resize if too large (max width 600px for email compatibility)
            max_width = 600
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

            # Convert to RGB if needed (remove alpha channel)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background

            # Save to BytesIO with compression
            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85, optimize=True)
            buffer.seek(0)

            # Convert to base64
            img_data = base64.b64encode(buffer.read()).decode('utf-8')
            header_img_html = f'''<tr>
                <td align="center" style="padding-bottom: 24px;">
                  <img src="data:image/jpeg;base64,{img_data}" width="600" style="width: 100%; max-width: 600px; height: auto; display: block;" alt="Daily Digest Header">
                </td>
              </tr>'''

        except Exception as e:
            print(f"⚠ Warning: Could not embed header image: {e}")
            header_img_html = ""

    # Build episode cards using table-based layout
    episode_cards_html = ""
    for i, episode in enumerate(episodes):
        podcast_name = episode['podcast_name']
        title = episode['title']
        video_id = episode['video_id']
        upload_date = episode['upload_date'].strftime('%B %d, %Y')
        description = descriptions.get(video_id, "New episode available.")

        # The episode slug is the sanitized title (folder name), not the video ID
        sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)
        encoded_podcast = urllib.parse.quote(podcast_name)
        encoded_slug = urllib.parse.quote(sanitized_title)
        summary_url = f"https://teahose.com/podcast/{encoded_podcast}/{encoded_slug}?ref=email"

        is_last = i == len(episodes) - 1
        padding_bottom = '0' if is_last else '24px'

        # Each episode card is a table for consistent rendering
        episode_cards_html += f'''
      <tr>
        <td style="padding-bottom: {padding_bottom};">
          <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{colors['card']}" style="background-color: {colors['card']}; border: 3px solid {colors['border']};">
            <tr>
              <td style="padding: 24px 16px;">
                <a href="{summary_url}" style="text-decoration: none; color: {colors['foreground']};">
                  <div style="color: {colors['muted_foreground']}; font-size: 14px; margin: 0 0 8px 0;">{upload_date}</div>
                  <div style="margin: 0 0 6px 0; font-size: 24px; font-weight: 700; letter-spacing: -0.01em; text-transform: uppercase; color: {colors['foreground']};">
                    {title}
                  </div>
                  <div style="color: {colors['muted_foreground']}; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 12px 0;">{podcast_name}</div>
                  <div style="color: {colors['foreground']}; font-size: 15px; line-height: 1.75; margin: 0;">
                    {description}
                  </div>
                </a>
              </td>
            </tr>
          </table>
        </td>
      </tr>'''

    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Podcast Digest - {date_str}</title>
</head>
<body style="margin: 0; padding: 0; background-color: {colors['background']};" bgcolor="{colors['background']}">
    <!-- Outer wrapper table for centering -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{colors['background']}" style="background-color: {colors['background']};">
      <tr>
        <td align="center" style="padding: 20px;">
          <!-- Main content table (600px width for compatibility) -->
          <table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="{colors['card']}" style="background-color: {colors['card']}; border: 3px solid {colors['border']}; max-width: 600px;">
            <tr>
              <td style="padding: 32px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: {colors['foreground']};">

                <!-- Header Image -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  {header_img_html}
                </table>

                <!-- Episode Count -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="color: {colors['muted_foreground']}; font-size: 14px; padding-bottom: 24px;">
                      <strong>{len(episodes)}</strong> new episode{"s" if len(episodes) != 1 else ""} published today
                    </td>
                  </tr>
                </table>

                <!-- Episode Cards -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  {episode_cards_html}
                </table>

                <!-- Footer -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top: 32px;">
                  <tr>
                    <td style="border-top: 1px solid {colors['muted_foreground']}; padding-top: 24px; font-size: 1px; line-height: 1px;">&nbsp;</td>
                  </tr>
                  <tr>
                    <td align="center" style="color: {colors['muted_foreground']}; font-size: 14px; padding-bottom: 8px;">
                      Discover the insights within each episode.
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="font-size: 14px;">
                      <a href="https://teahose.com?ref=email" style="color: {colors['accent']}; text-decoration: underline;">teahose.com</a>
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
          </table>
          <!-- End main content table -->
        </td>
      </tr>
    </table>
    <!-- End outer wrapper -->
</body>
</html>'''

    return html

def main():
    print("📧 Generating daily email digest...")

    # Load podcast status
    status_data = load_podcast_status()

    # Get episodes from last 24 hours
    print("   Finding episodes from last 24 hours...")
    episodes = get_episodes_from_last_day(status_data)

    if not episodes:
        print("   No episodes found in the last 24 hours.")
        return

    print(f"   Found {len(episodes)} episode(s)")

    # Create output directory
    DAILY_EMAILS_DIR.mkdir(exist_ok=True)

    # Generate date string
    date_str = datetime.now().strftime("%B %d, %Y")
    file_date_str = datetime.now().strftime("%Y-%m-%d")

    # Generate episode descriptions
    print("   Generating episode descriptions...")
    descriptions = generate_episode_descriptions(episodes)

    # Generate header image
    print("   Generating header image...")
    header_image_path = DAILY_EMAILS_DIR / f"daily_digest_{file_date_str}_header.png"
    generate_header_image(episodes, date_str, header_image_path)

    # Generate HTML email
    print("   Generating HTML email...")
    html_content = generate_html_email(episodes, descriptions, header_image_path, date_str)

    # Save HTML file
    html_file_path = DAILY_EMAILS_DIR / f"daily_digest_{file_date_str}.html"
    with open(html_file_path, 'w') as f:
        f.write(html_content)

    print(f"\n✓ Daily email generated!")
    print(f"   HTML file: {html_file_path}")
    print(f"   Header image: {header_image_path}")
    print(f"\n   Open the HTML file in a browser to preview, then copy-paste into your email client.")

if __name__ == "__main__":
    main()
