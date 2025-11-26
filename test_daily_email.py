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

def get_episodes_from_last_day():
    """Get all episodes published in the last 24 hours with status = summarized."""
    if not PODCAST_STATUS_FILE.exists():
        print(f"Error: {PODCAST_STATUS_FILE} not found")
        return []

    with open(PODCAST_STATUS_FILE, 'r') as f:
        status_data = json.load(f)

    cutoff_date = datetime.now() - timedelta(days=1)
    episodes = []

    for podcast_url, podcast_data in status_data.get("podcasts", {}).items():
        podcast_name = podcast_data.get("podcast_name", "Unknown")

        if not podcast_name or podcast_name == "None" or podcast_name == "One-off Episodes":
            continue

        for video_id, episode_data in podcast_data.get("episodes", {}).items():
            if episode_data.get("status") != "summarized":
                continue

            upload_date_str = episode_data.get("upload_date")
            if not upload_date_str or upload_date_str == "0":
                continue

            try:
                upload_date = datetime.strptime(upload_date_str, "%Y%m%d")
            except ValueError:
                continue

            if upload_date < cutoff_date:
                continue

            title = episode_data.get("title", "Unknown")
            sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)
            episode_folder = PODCAST_WORK_DIR / podcast_name / sanitized_title
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


def generate_header_image(episodes, date_str, output_path):
    """Generate header image using Google Gemini."""
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

FOOTER BANNER: Bold black text "THE DAILY TEAHOSE - {date_str}" on cream background strip

REQUIREMENTS:
- All {num_topics} panels clearly visible and equal-sized
- Warm cream aged paper background throughout
- Bold red/yellow/blue accents only (no orange, no bright green)
- All text UPPERCASE and highly legible
- Portrait orientation (taller than wide)
- Professional vintage newspaper comic quality"""

    try:
        client = genai.Client(api_key=google_api_key)

        # Use gemini-3-pro-image-preview (Nano Banana Pro) - same as generate_daily_email.py
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        # Extract and save the generated image
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(output_path))
                print(f"Header image generated: {output_path}")
                return output_path

        print("Warning: No image data in response")
        return None
    except Exception as e:
        print(f"Warning: Could not generate header image: {e}")
        return None


def generate_email_html(episodes, date_str, header_image_path=None):
    """Generate HTML email content."""
    import base64
    from PIL import Image
    from io import BytesIO

    # Process header image if provided
    header_img_html = ""
    if header_image_path and Path(header_image_path).exists():
        try:
            img = Image.open(header_image_path)
            max_width = 800
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
            header_img_html = f'<img src="data:image/jpeg;base64,{img_data}" style="width: 100%; max-width: 800px; height: auto; margin: 0 0 32px 0;" alt="Daily Teahose Header">'
        except Exception as e:
            print(f"Warning: Could not embed header image: {e}")

    colors = {
        'background': '#f7f4f0',
        'foreground': '#1a1a1a',
        'card': '#fffefa',
        'muted_foreground': '#555555',
        'accent': '#c41e3a',
        'border': '#1a1a1a',
    }

    episode_cards = ""
    for index, episode in enumerate(episodes):
        upload_date = episode['upload_date'].strftime('%B %d, %Y')
        sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', episode['title'])
        encoded_podcast = requests.utils.quote(episode['podcast_name'])
        encoded_slug = requests.utils.quote(sanitized_title)
        summary_url = f"https://teahose.com/podcast/{encoded_podcast}/{encoded_slug}"

        is_last = index == len(episodes) - 1
        margin_bottom = '0' if is_last else '24px'

        participants_html = ''
        if episode.get('participants'):
            participants_html = f'<p style="color: {colors["foreground"]}; font-size: 14px; margin: 0 0 8px 0;">{episode["participants"]}</p>'

        episode_cards += f"""
        <a href="{summary_url}" style="text-decoration: none; display: block;">
            <div style="background: {colors['card']}; padding: 24px 16px; margin-bottom: {margin_bottom}; border: 3px solid {colors['border']}; box-shadow: 4px 4px 0 {colors['border']}; border-radius: 0; cursor: pointer;">
                <h2 style="margin: 0 0 6px 0; font-size: 24px; font-weight: 700; letter-spacing: -0.01em; text-transform: uppercase; color: {colors['foreground']};">
                    {episode['title']}
                </h2>
                <p style="color: {colors['muted_foreground']}; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 4px 0;">{episode['podcast_name']}</p>
                {participants_html}
                <p style="color: {colors['muted_foreground']}; font-size: 12px; margin: 0 0 12px 0;">{upload_date}</p>
                <p style="color: {colors['foreground']}; font-size: 15px; line-height: 1.75; margin: 0;">
                    {episode.get('description', 'New episode available.')}
                </p>
            </div>
        </a>"""

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Daily Teahose - {date_str}</title>
</head>
<body style="font-family: 'Geist', -apple-system, BlinkMacSystemFont, system-ui, sans-serif; line-height: 1.6; color: {colors['foreground']}; max-width: 896px; margin: 0 auto; padding: 10px; background-color: {colors['background']};">

    <div style="background: {colors['card']}; padding: 32px 20px; border: 3px solid {colors['border']}; box-shadow: 4px 4px 0 {colors['border']}; border-radius: 0;">

        {header_img_html}

        {episode_cards}
    </div>

    <div style="text-align: center; padding: 32px 20px; color: {colors['muted_foreground']}; font-size: 14px;">
        <p style="margin: 0;">
            A distillation of insight from the highest signal technology and entrepreneurship podcasts.<br>
            <a href="https://teahose.com" style="color: {colors['accent']}; text-decoration: underline; text-decoration-thickness: 2px; margin-top: 16px; display: inline-block;">Teahose.com</a>
        </p>
    </div>

</body>
</html>"""


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
        print("Usage: python test_daily_email.py <email_address>")
        sys.exit(1)

    to_email = sys.argv[1]
    print(f"Sending test daily email to {to_email}...")

    # Get episodes
    print("Finding episodes from last 24 hours...")
    episodes = get_episodes_from_last_day()

    if not episodes:
        print("No episodes found in the last 24 hours. Creating test with empty content.")
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

    # Generate header image
    print("Generating header image...")
    header_image_path = Path("./daily_emails") / f"test_header_{datetime.now().strftime('%Y-%m-%d')}.png"
    header_image_path.parent.mkdir(exist_ok=True)
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
