#!/usr/bin/env python3
"""
Test script to send a daily email to a specific address.
Usage: python test_daily_email.py altmbr@gmail.com
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests

load_dotenv()

PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_WORK_DIR = Path("./podcast_work")
SENDGRID_API_URL = "https://api.sendgrid.com/v3/mail/send"
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

def get_episodes_from_last_day(days=1):
    """Get all episodes published in the last N days with status = summarized."""
    if not PODCAST_STATUS_FILE.exists():
        print(f"Error: {PODCAST_STATUS_FILE} not found")
        return []

    with open(PODCAST_STATUS_FILE, 'r') as f:
        status_data = json.load(f)

    cutoff_date = datetime.now() - timedelta(days=days)
    episodes = []

    for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
        podcast_name = podcast_data.get("podcast_name", "Unknown")

        if not podcast_name or podcast_name == "None":
            continue

        for video_id, episode_data in podcast_data.get("episodes", {}).items():
            if episode_data.get("status") != "summarized":
                continue

            upload_date_str = episode_data.get("upload_date")
            if not upload_date_str or upload_date_str == "0":
                continue

            try:
                # Parse date and set to noon UTC to avoid edge cases (matches cron behavior)
                upload_date = datetime.strptime(upload_date_str, "%Y%m%d")
                upload_date = upload_date.replace(hour=12, minute=0, second=0, microsecond=0)
            except ValueError:
                continue

            if upload_date < cutoff_date:
                continue

            title = episode_data.get("title", "Unknown")
            sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)

            # Try podcast_name from JSON first, then try "one off episodes" for One-off Episodes
            episode_folder = PODCAST_WORK_DIR / podcast_name / sanitized_title
            if not episode_folder.exists() and podcast_name == "One-off Episodes":
                episode_folder = PODCAST_WORK_DIR / "one off episodes" / sanitized_title

            summary_file = episode_folder / "summary.md"

            if not summary_file.exists():
                continue

            # Extract participants from summary file
            participants = None
            try:
                with open(summary_file, 'r') as f:
                    summary_content = f.read()
                participants_match = re.search(r'\*\*Participants:\*\*\s*(.+)', summary_content)
                if participants_match:
                    participants = participants_match.group(1).strip()
            except Exception:
                pass

            episodes.append({
                "podcast_name": podcast_name,
                "title": title,
                "video_id": video_id,
                "upload_date": upload_date,
                "summary_path": summary_file,
                "video_url": f"https://www.youtube.com/watch?v={video_id}",
                "region": episode_data.get("region", "Western"),
                "participants": participants
            })

    episodes.sort(key=lambda x: x["upload_date"], reverse=True)
    return episodes


def extract_key_themes(summary_path):
    """Extract key themes and contrarian perspectives sections from summary."""
    try:
        with open(summary_path, 'r') as f:
            content = f.read()

        # Extract both Key Themes and Contrarian Perspectives sections
        lines = content.split('\n')
        in_relevant_section = False
        extracted_content = []

        for line in lines:
            # Start capturing at Key Themes
            if re.match(r'^##?\s*(?:1\.|A\.)\s*Key\s+Themes', line, re.IGNORECASE):
                in_relevant_section = True
                continue
            # Continue capturing at Contrarian Perspectives
            if re.match(r'^##?\s*(?:2\.|B\.)\s*Contrarian\s+Perspectives?', line, re.IGNORECASE):
                in_relevant_section = True
                continue
            if in_relevant_section:
                # Stop at other major sections (Companies, People, etc)
                if re.match(r'^##\s*(?:3\.|4\.|C\.|D\.)', line):
                    break
                extracted_content.append(line)

        if extracted_content:
            return '\n'.join(extracted_content).strip()[:3000]
        return content[:3000]
    except Exception:
        return ""


def generate_description(episode):
    """Generate pithy description using Claude."""
    if not ANTHROPIC_API_KEY:
        return "New episode available."

    summary_excerpt = extract_key_themes(episode['summary_path'])
    if not summary_excerpt:
        return "New episode available."

    prompt = f"""Write a pithy, signal-dense summary (max 45 words) of this podcast episode. Cover: main discussion topics, key themes, and any contrarian insights. Be specific and punchy.

Episode: {episode['title']}

Key themes:
{summary_excerpt}

Summary:"""

    try:
        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_API_KEY,
                'anthropic-version': '2023-06-01'
            },
            json={
                'model': 'claude-sonnet-4-5-20250929',
                'max_tokens': 150,
                'messages': [{'role': 'user', 'content': prompt}]
            }
        )
        data = response.json()
        return data.get('content', [{}])[0].get('text', 'New episode available.').strip()
    except Exception as e:
        print(f"Warning: Could not generate description: {e}")
        return "New episode available."


# Feature flag for header image style
# true = new composite style with unified scene, nametags, worn paper texture
# false = old panel-based style with separate panels per episode
# To revert: set USE_COMPOSITE_HEADER = False
USE_COMPOSITE_HEADER = True


def generate_visual_concept(episodes):
    """Use Claude to generate a unified visual concept from all episodes."""
    if not ANTHROPIC_API_KEY:
        return 'A collage of tech industry themes including AI, business strategy, and innovation.'

    # Format episode information for Claude
    episodes_text = []
    for i, ep in enumerate(episodes[:5], 1):
        participants_str = f" [{ep.get('participants', '')}]" if ep.get('participants') else ""
        episodes_text.append(f"{i}. {ep['title']}{participants_str}\n   {ep.get('description', '')}")

    episodes_formatted = "\n\n".join(episodes_text)

    prompt = f"""You are creating a vintage 1950s newspaper-style comic illustration that combines visual elements from {len(episodes[:5])} podcast episodes into ONE unified composition.

Here are the episodes:

{episodes_formatted}

Create a detailed description of a single unified illustration that combines visual metaphors representing all episodes. The illustration should:
- Blend elements from all episodes into one cohesive scene (like a vintage political cartoon)
- Use overlapping figures, symbols, and objects
- Include human figures in 1950s comic book style representing the speakers/topics (IMPORTANT: mention participant names when known so they can be labeled)
- Use symbolic objects (books, technology, microphones, abstract concepts)
- Create visual interest and narrative density

Describe the unified composition in 3-4 sentences. Be specific about what visual elements appear and how they interact. When describing human figures, include the participant names from the episode metadata."""

    try:
        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers={
                'Content-Type': 'application/json',
                'x-api-key': ANTHROPIC_API_KEY,
                'anthropic-version': '2023-06-01'
            },
            json={
                'model': 'claude-sonnet-4-5-20250929',
                'max_tokens': 300,
                'messages': [{'role': 'user', 'content': prompt}]
            }
        )
        data = response.json()
        return data.get('content', [{}])[0].get('text', '').strip() or 'A collage of tech industry themes including AI, business strategy, and innovation.'
    except Exception as e:
        print(f"Warning: Could not generate visual concept: {e}")
        return 'A collage of tech industry themes including AI, business strategy, and innovation.'


def generate_composite_header_image(episodes, date_str, output_path):
    """Generate composite header image with unified scene and nametags."""
    try:
        from google import genai
    except ImportError:
        print("Installing google-genai...")
        import subprocess
        subprocess.run(["pip", "install", "-q", "google-genai"], check=True)
        from google import genai

    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Warning: GOOGLE_API_KEY not set")
        return None

    # Generate visual concept using Claude
    print("  → Generating visual concept with Claude...")
    visual_concept = generate_visual_concept(episodes)
    print(f"  → Visual concept: {visual_concept[:100]}...")

    prompt = f"""Create a vintage 1950s newspaper-style composite illustration for a podcast digest header.

CRITICAL LAYOUT REQUIREMENTS:
- LANDSCAPE format: EXACTLY 750 pixels wide × 500 pixels tall
- Single unified composition (NOT separate panels)
- NO footer text or banner - the illustration should fill the entire image
- Warm aged cream paper background (#f7f4f0)
- Thick black border (3px) around entire image

ARTISTIC STYLE - Vintage 1950s Roy Lichtenstein pop art:
- BACKGROUND: Warm aged cream paper (#f7f4f0) with subtle halftone texture
- PAPER TEXTURE: Add worn, aged paper effect with slight yellowing, subtle creases, and soft edge wear to give authentic vintage newspaper feel
- COLORS: Bold pop art accents - cardinal red (#c41e3a), golden yellow (#f4c430), deep blue (#2d5a7b)
- SHADOWS: Black comic drop shadows (not brown)
- TEXTURE: Ben Day halftone dots for shading, stipple patterns
- OUTLINES: Thick black outlines (3px) around all major elements
- OVERALL: Clean vintage newspaper comic aesthetic with worn paper texture

VISUAL COMPOSITION:
{visual_concept}

SPECIFIC REQUIREMENTS:
- Human figures in vintage comic book style with halftone shading
- NAMETAGS: Each human figure MUST wear a nametag on their chest with their name in BIG, BOLD, LEGIBLE UPPERCASE letters (like "ELON MUSK", "SAM ALTMAN", etc.)
- Nametags should be rectangular/rounded white/cream labels with thick black outlines and large black text
- Symbolic objects (books, technology, microphones, brains, buildings, etc.)
- Elements should blend and overlap to create narrative density
- Dynamic composition with depth and visual flow

COLOR USAGE:
- Overall background: warm cream (#f7f4f0)
- Main subjects use bold accent colors (cardinal red, golden yellow, deep blue)
- Supporting elements use lighter tints (soft red #fdf5f5, soft yellow #fffcf0, soft blue #f5f8fa)
- All borders and outlines: true black (#1a1a1a)
- Ben Day dot patterns for shading and depth

OVERALL AESTHETIC:
- Sophisticated vintage newspaper illustration with worn paper texture
- Educational and thought-provoking
- Multiple narratives visible in single unified composition
- Professional print quality with sharp lines
- Perfect for email newsletter banner"""

    try:
        client = genai.Client(api_key=google_api_key)

        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(output_path))
                print(f"Composite header image generated: {output_path}")
                return output_path

        print("Warning: No image data in response")
        return None
    except Exception as e:
        print(f"Warning: Could not generate composite header image: {e}")
        return None


def generate_panel_header_image(episodes, date_str, output_path):
    """OLD STYLE: Panel-based header image (set USE_COMPOSITE_HEADER = False to use this)."""
    try:
        from google import genai
    except ImportError:
        print("Installing google-genai...")
        import subprocess
        subprocess.run(["pip", "install", "-q", "google-genai"], check=True)
        from google import genai

    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Warning: GOOGLE_API_KEY not set")
        return None

    # Extract topics from episode titles
    topics = []
    for ep in episodes[:6]:
        title = ep['title']
        title = re.sub(r'^.*?:\s*', '', title)
        title = re.split(r'\s*[\|\-]\s*', title)[0]
        if len(title) > 50:
            title = title[:47] + "..."
        topics.append(title)

    num_topics = len(topics)

    # Determine layout
    if num_topics == 1:
        layout = "1 large panel filling the entire image"
        panel_desc = f'Single Panel: "{topics[0]}"'
    elif num_topics == 2:
        layout = "2 panels stacked vertically"
        panel_desc = f'Panel 1: "{topics[0]}"\nPanel 2: "{topics[1]}"'
    elif num_topics == 3:
        layout = "3 panels stacked vertically"
        panel_desc = f'Panel 1: "{topics[0]}"\nPanel 2: "{topics[1]}"\nPanel 3: "{topics[2]}"'
    elif num_topics == 4:
        layout = "4 panels in a 2x2 grid"
        panel_desc = '\n'.join([f'Panel {i+1}: "{t}"' for i, t in enumerate(topics)])
    elif num_topics == 5:
        layout = "5 panels: 1 wide panel at top spanning full width, then 2 rows of 2 panels each below"
        panel_desc = '\n'.join([f'Panel {i+1}: "{t}"' for i, t in enumerate(topics)])
    else:
        layout = "6 panels in a 2x3 grid (2 columns, 3 rows)"
        panel_desc = '\n'.join([f'Panel {i+1}: "{t}"' for i, t in enumerate(topics)])

    prompt = f"""Create a vintage 1950s newspaper-style comic header for a daily podcast digest.

LAYOUT: {layout} in PORTRAIT format (taller than wide).

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

NO FOOTER - illustration fills the entire image

REQUIREMENTS:
- All {num_topics} panels clearly visible and equal-sized
- Warm cream aged paper background throughout
- Bold red/yellow/blue accents only (no orange, no bright green)
- All text UPPERCASE and highly legible
- Portrait orientation (taller than wide)
- Professional vintage newspaper comic quality"""

    try:
        client = genai.Client(api_key=google_api_key)

        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(output_path))
                print(f"Panel header image generated: {output_path}")
                return output_path

        print("Warning: No image data in response")
        return None
    except Exception as e:
        print(f"Warning: Could not generate panel header image: {e}")
        return None


def generate_header_image(episodes, date_str, output_path):
    """Router function to pick header image style based on feature flag."""
    if USE_COMPOSITE_HEADER:
        return generate_composite_header_image(episodes, date_str, output_path)
    else:
        return generate_panel_header_image(episodes, date_str, output_path)


def generate_email_html(episodes, date_str, header_image_path=None):
    """Generate HTML email content using table-based layout for cross-client compatibility."""
    import base64
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
        'background': '#f7f4f0',
        'foreground': '#1a1a1a',
        'card': '#fffefa',
        'muted_foreground': '#555555',
        'accent': '#c41e3a',
        'border': '#1a1a1a',
    }

    # Process header image if provided
    header_img_html = ""
    if header_image_path and Path(header_image_path).exists():
        try:
            img = Image.open(header_image_path)
            # Resize to 600px for email compatibility
            max_width = 600
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = background

            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=85, optimize=True)
            buffer.seek(0)
            img_data = base64.b64encode(buffer.read()).decode('utf-8')
            header_img_html = f'''<tr>
                <td align="center" style="padding-bottom: 24px;">
                  <img src="data:image/jpeg;base64,{img_data}" width="600" style="width: 100%; max-width: 600px; height: auto; display: block;" alt="Daily Teahose Header">
                </td>
              </tr>'''
        except Exception as e:
            print(f"Warning: Could not embed header image: {e}")

    # Build episode cards using table-based layout
    episode_cards = ""
    for index, episode in enumerate(episodes):
        upload_date = episode['upload_date'].strftime('%B %d, %Y')
        sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', episode['title'])
        encoded_podcast = requests.utils.quote(episode['podcast_name'])
        encoded_slug = requests.utils.quote(sanitized_title)
        summary_url = f"https://teahose.com/podcast/{encoded_podcast}/{encoded_slug}?ref=email"

        is_last = index == len(episodes) - 1
        padding_bottom = '0' if is_last else '24px'

        # Use <div> instead of <p> inside table cells for Gmail compatibility
        participants_html = ''
        if episode.get('participants'):
            participants_html = f'<div style="color: {colors["foreground"]}; font-size: 14px; margin: 0 0 8px 0; padding: 0;">{episode["participants"]}</div>'

        # Each episode card is a table for consistent rendering
        episode_cards += f'''
      <tr>
        <td style="padding-bottom: {padding_bottom};">
          <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{colors['card']}" style="background-color: {colors['card']}; border: 3px solid {colors['border']};">
            <tr>
              <td style="padding: 24px 16px;">
                <a href="{summary_url}" style="text-decoration: none; color: {colors['foreground']};">
                  <div style="margin: 0 0 6px 0; font-size: 24px; font-weight: 700; letter-spacing: -0.01em; text-transform: uppercase; color: {colors['foreground']};">
                    {episode['title']}
                  </div>
                  <div style="color: {colors['muted_foreground']}; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 4px 0;">{episode['podcast_name']}</div>
                  {participants_html}
                  <div style="color: {colors['muted_foreground']}; font-size: 12px; margin: 0 0 12px 0;">{upload_date}</div>
                  <div style="color: {colors['foreground']}; font-size: 15px; line-height: 1.75; margin: 0;">
                    {episode.get('description', 'New episode available.')}
                  </div>
                </a>
              </td>
            </tr>
          </table>
        </td>
      </tr>'''

    return f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Daily Teahose - {date_str}</title>
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

                <!-- Header Title -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td align="center" style="padding-bottom: 20px;">
                      <a href="https://teahose.com?ref=email" style="text-decoration: none; color: {colors['foreground']};">
                        <div style="margin: 0; font-size: 28px; font-weight: 900; text-transform: uppercase; color: {colors['foreground']}; letter-spacing: -0.02em;">
                          THE DAILY TEAHOSE
                        </div>
                      </a>
                    </td>
                  </tr>
                </table>

                <!-- Signup CTA Box - table-based for compatibility -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td align="center" style="padding-bottom: 24px;">
                      <table cellpadding="0" cellspacing="0" border="0" style="border: 2px solid {colors['border']};">
                        <tr>
                          <td style="padding: 12px 16px; font-size: 14px; color: {colors['foreground']};">
                            Forwarded this email? Get daily summaries of top tech and business podcasts.
                          </td>
                          <td style="padding: 12px 16px 12px 8px; white-space: nowrap;">
                            <table cellpadding="0" cellspacing="0" border="0" bgcolor="{colors['foreground']}" style="background-color: {colors['foreground']};">
                              <tr>
                                <td style="padding: 8px 16px; white-space: nowrap;">
                                  <a href="https://teahose.com?ref=email" style="color: {colors['card']}; text-decoration: none; font-weight: 600; font-size: 14px; white-space: nowrap;">Sign&nbsp;Up</a>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>

                <!-- Divider -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="border-top: 1px solid {colors['muted_foreground']}; padding-bottom: 24px; font-size: 1px; line-height: 1px;">&nbsp;</td>
                  </tr>
                </table>

                <!-- Header Image -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  {header_img_html}
                </table>

                <!-- Episode Cards -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  {episode_cards}
                </table>

                <!-- Footer -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top: 32px;">
                  <tr>
                    <td style="border-top: 1px solid {colors['muted_foreground']}; padding-top: 24px; font-size: 1px; line-height: 1px;">&nbsp;</td>
                  </tr>
                  <tr>
                    <td align="center" style="color: {colors['muted_foreground']}; font-size: 13px; line-height: 1.6; padding-bottom: 12px;">
                      A distillation of insight from the highest signal technology and entrepreneurship podcasts.
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="color: {colors['muted_foreground']}; font-size: 13px;">
                      <a href="https://teahose.com?ref=email" style="color: {colors['accent']}; text-decoration: underline;">Teahose.com</a>
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


def send_email(to_email, subject, html_content):
    """Send email via SendGrid."""
    if not SENDGRID_API_KEY:
        print("Error: SENDGRID_API_KEY not set in .env")
        return False

    response = requests.post(
        SENDGRID_API_URL,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {SENDGRID_API_KEY}'
        },
        json={
            'personalizations': [{'to': [{'email': to_email}]}],
            'from': {
                'email': 'agent@teahose.com',
                'name': 'The Daily Teahose'
            },
            'subject': subject,
            'content': [{'type': 'text/html', 'value': html_content}]
        }
    )

    if response.status_code == 202:
        return True
    else:
        print(f"SendGrid error: {response.status_code} - {response.text}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python test_daily_email.py <email_address> [days]")
        print("  days: number of days to look back for episodes (default: 1)")
        sys.exit(1)

    to_email = sys.argv[1]
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    print(f"Sending test daily email to {to_email}...")

    # Get episodes
    print(f"Finding episodes from last {days} day(s)...")
    episodes = get_episodes_from_last_day(days=days)

    if not episodes:
        print(f"No episodes found in the last {days} day(s). Creating test with empty content.")
        # Still send a test email even with no episodes
        date_str = datetime.now().strftime("%B %d, %Y")
        html_content = f"""<!DOCTYPE html>
<html>
<head><title>The Daily Teahose - {date_str}</title></head>
<body style="font-family: sans-serif; padding: 20px;">
<h1>The Daily Teahose</h1>
<p>No new episodes today. This is a test email.</p>
<p><a href="https://teahose.com">teahose.com</a></p>
</body>
</html>"""
        subject = f"[TEST] The Daily Teahose - {date_str}"
        success = send_email(to_email, subject, html_content)
        if success:
            print(f"Test email sent to {to_email}")
        else:
            print("Failed to send test email")
        return

    print(f"Found {len(episodes)} episode(s)")

    # Generate descriptions
    print("Generating episode descriptions...")
    for episode in episodes:
        print(f"  - {episode['title'][:50]}...")
        episode['description'] = generate_description(episode)

    # Generate date string
    date_str = datetime.now().strftime("%B %d, %Y")

    # Check for existing placeholder image for faster testing
    header_image_path = Path("./daily_emails") / f"test_header_{datetime.now().strftime('%Y-%m-%d')}.png"
    header_image_path.parent.mkdir(exist_ok=True)

    if header_image_path.exists():
        print(f"Using existing header: {header_image_path.name}")
    else:
        # Generate new header image
        print("Generating header image...")
        generate_header_image(episodes, date_str, header_image_path)

    # Generate HTML
    html_content = generate_email_html(episodes, date_str, header_image_path)
    subject = f"The Daily Teahose - {date_str}"

    # Send
    print(f"Sending email...")
    success = send_email(to_email, subject, html_content)

    if success:
        print(f"Email sent successfully to {to_email}")
    else:
        print("Failed to send email")


if __name__ == "__main__":
    main()
