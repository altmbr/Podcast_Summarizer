#!/usr/bin/env python3
"""
Test script for generating half-height composite header images.
Creates test images combining elements from 5 episodes per image.
"""

import os
import json
import random
import re
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
PODCAST_STATUS_FILE = Path("./podcast_status.json")
PODCAST_WORK_DIR = Path("./podcast_work")
TEST_OUTPUT_DIR = Path("./test_composite_headers")
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"

def load_podcast_status():
    """Load podcast status from JSON file"""
    if not PODCAST_STATUS_FILE.exists():
        print(f"❌ Error: {PODCAST_STATUS_FILE} not found")
        return None

    with open(PODCAST_STATUS_FILE, 'r') as f:
        return json.load(f)

def get_all_summarized_episodes(status_data):
    """Get all summarized episodes with their summary paths"""
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

            title = episode_data.get("title", "Unknown")
            sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)

            # Find the summary file
            episode_folder = PODCAST_WORK_DIR / podcast_name / sanitized_title
            summary_file = episode_folder / "summary.md"

            if not summary_file.exists():
                continue

            episodes.append({
                "podcast_name": podcast_name,
                "title": title,
                "video_id": video_id,
                "summary_path": summary_file,
            })

    return episodes

def extract_key_themes_from_summary(summary_path):
    """Extract Key Themes section from summary file (same as cron)"""
    try:
        with open(summary_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the Key Themes section
        lines = content.split('\n')
        in_relevant_section = False
        extracted_content = []

        for line in lines:
            # Start capturing at Key Themes
            if re.search(r'^##?\s*(?:1\.|A\.)\s*Key\s+Themes', line, re.IGNORECASE):
                in_relevant_section = True
                continue
            # Continue capturing at Contrarian Perspectives
            if re.search(r'^##?\s*(?:2\.|B\.)\s*Contrarian\s+Perspectives?', line, re.IGNORECASE):
                in_relevant_section = True
                continue
            if in_relevant_section:
                # Stop at other major sections
                if re.search(r'^##\s*(?:3\.|4\.|C\.|D\.)', line):
                    break
                extracted_content.append(line)

        if extracted_content:
            return '\n'.join(extracted_content).strip()[:3000]
        return content[:3000]

    except Exception as e:
        print(f"⚠ Warning: Could not read summary from {summary_path}: {e}")
        return None

def extract_participants_from_summary(summary_path):
    """Extract participants from summary metadata"""
    try:
        with open(summary_path, 'r', encoding='utf-8') as f:
            # Read first 15 lines to find metadata
            for _ in range(15):
                line = f.readline()
                if not line:
                    break
                if 'Participants:' in line or '**Participants:**' in line:
                    # Extract participants after the colon
                    participants = re.sub(r'.*?\*?\*?Participants:\*?\*?\s*', '', line).strip()
                    return participants
        return None
    except Exception as e:
        print(f"⚠ Warning: Could not extract participants from {summary_path}: {e}")
        return None

def generate_episode_description(episode, anthropic_client):
    """Generate pithy description using Claude (same as cron)"""
    summary_excerpt = extract_key_themes_from_summary(episode['summary_path'])

    if not summary_excerpt:
        return "New episode available."

    prompt = f"""Write a pithy, signal-dense summary (max 45 words) of this podcast episode. Cover: main discussion topics, key themes, and any contrarian insights. Be specific and punchy.

Episode: {episode['title']}

Key themes:
{summary_excerpt}

Summary:"""

    try:
        response = anthropic_client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"⚠ Warning: Could not generate description for {episode['title']}: {e}")
        return "New episode available."

def generate_visual_concept(episodes_with_descriptions, anthropic_client):
    """Use Claude to generate a unified visual concept from all episodes"""
    # Format episode information for Claude
    episodes_text = []
    for i, ep in enumerate(episodes_with_descriptions[:5], 1):
        participants = ep.get('participants', '')
        participants_str = f" [{participants}]" if participants else ""
        episodes_text.append(f"{i}. {ep['title']}{participants_str}\n   {ep['description']}")

    episodes_formatted = "\n\n".join(episodes_text)

    # Ask Claude to generate a unified visual concept
    meta_prompt = f"""You are creating a vintage 1950s newspaper-style comic illustration that combines visual elements from 5 podcast episodes into ONE unified composition.

Here are the 5 episodes:

{episodes_formatted}

Create a detailed description of a single unified illustration that combines visual metaphors representing all 5 episodes. The illustration should:
- Blend elements from all episodes into one cohesive scene (like a vintage political cartoon)
- Use overlapping figures, symbols, and objects
- Include human figures in 1950s comic book style representing the speakers/topics (IMPORTANT: mention participant names when known so they can be labeled)
- Use symbolic objects (books, technology, microphones, abstract concepts)
- Create visual interest and narrative density

Describe the unified composition in 3-4 sentences. Be specific about what visual elements appear and how they interact. When describing human figures, include the participant names from the episode metadata."""

    try:
        response = anthropic_client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=300,
            messages=[{"role": "user", "content": meta_prompt}]
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"⚠ Warning: Could not generate visual concept: {e}")
        return "A collage of tech industry themes including AI, business strategy, and innovation."

def create_image_generation_prompt(visual_concept, date_str):
    """Create the final prompt for Gemini image generation"""
    prompt = f"""Create a vintage 1950s newspaper-style composite illustration for a podcast digest header.

CRITICAL LAYOUT REQUIREMENTS:
- SQUARE format: EXACTLY 750 pixels × 750 pixels (1:1 aspect ratio)
- Single unified composition (NOT separate panels)
- FOOTER at bottom: Bold text "THE DAILY TEAHOSE - {date_str}" centered on cream background strip
- Main illustration fills most of the space above the footer
- Warm aged cream paper background (#f7f4f0)
- Thick black border (3px) around entire image

ARTISTIC STYLE - Vintage 1950s Roy Lichtenstein pop art:
- BACKGROUND: Warm aged cream paper (#f7f4f0) with subtle halftone texture
- COLORS: Bold pop art accents - cardinal red (#c41e3a), golden yellow (#f4c430), deep blue (#2d5a7b)
- SHADOWS: Black comic drop shadows (not brown)
- TEXTURE: Ben Day halftone dots for shading, stipple patterns
- OUTLINES: Thick black outlines (3px) around all major elements
- OVERALL: Clean vintage newspaper comic aesthetic

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

FOOTER BANNER:
- Bold black text: "THE DAILY TEAHOSE - {date_str}"
- Centered at bottom on cream background
- Clean, prominent, readable

OVERALL AESTHETIC:
- Sophisticated vintage newspaper illustration
- Educational and thought-provoking
- Multiple narratives visible in single unified composition
- Professional print quality with sharp lines
- Perfect for email newsletter banner"""

    return prompt

def generate_composite_header_image(episodes_with_descriptions, test_num, image_num, output_path):
    """
    Generate a composite header image using Google Gemini Nano Banana Pro.

    Args:
        episodes_with_descriptions: List of 5 episodes with title, participants, description
        test_num: Test number (1-3)
        image_num: Image number (1-3)
        output_path: Where to save the image

    Returns:
        bool: True if successful
    """
    try:
        from google import genai
        from anthropic import Anthropic
    except ImportError:
        print("⚠ Installing required packages...")
        import subprocess
        subprocess.run(["pip", "install", "-q", "google-genai", "anthropic"], check=True)
        from google import genai
        from anthropic import Anthropic

    # Initialize Anthropic client
    anthropic_client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Generate unified visual concept using Claude
    print(f"  → Generating visual concept with Claude...")
    visual_concept = generate_visual_concept(episodes_with_descriptions, anthropic_client)
    print(f"  → Visual concept: {visual_concept[:100]}...")

    # Create image generation prompt
    date_str = datetime.now().strftime("%B %d, %Y").upper()
    prompt = create_image_generation_prompt(visual_concept, date_str)

    print(f"\n{'='*80}")
    print(f"Test {test_num}, Image {image_num} - Full Prompt:")
    print(f"{'='*80}")
    print(prompt)
    print(f"{'='*80}\n")

    try:
        google_api_key = os.environ.get("GOOGLE_API_KEY")
        if not google_api_key:
            print("❌ Error: GOOGLE_API_KEY not set in .env")
            return False

        client = genai.Client(api_key=google_api_key)

        print(f"🎨 Generating Test {test_num}, Image {image_num} with Gemini...")

        # Use Nano Banana Pro
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        # Extract and save the generated image
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(str(output_path))
                print(f"✓ Saved: {output_path}")
                return True

        print("⚠ Warning: No image data in response")
        return False

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("🎨 Testing Composite Header Image Generation")
    print("=" * 80)

    # Validate API keys
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ Error: ANTHROPIC_API_KEY not set in .env")
        return
    if not os.environ.get("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not set in .env")
        return

    # Initialize Anthropic client
    from anthropic import Anthropic
    anthropic_client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Load podcast status
    status_data = load_podcast_status()
    if not status_data:
        return

    # Get all summarized episodes
    all_episodes = get_all_summarized_episodes(status_data)

    if len(all_episodes) < 15:
        print(f"❌ Error: Need at least 15 episodes for testing, found {len(all_episodes)}")
        return

    print(f"✓ Found {len(all_episodes)} summarized episodes")

    # Shuffle and group all episodes into batches of 5
    random.shuffle(all_episodes)
    batches = [all_episodes[i:i+5] for i in range(0, len(all_episodes), 5)]

    print(f"✓ Grouped into {len(batches)} batches of 5 episodes each")

    # Show all batches
    print("\n📊 All Episode Batches:")
    print("=" * 80)
    for batch_num, batch in enumerate(batches, 1):
        print(f"\nBatch {batch_num}:")
        for i, ep in enumerate(batch, 1):
            print(f"  {i}. {ep['podcast_name']}: {ep['title'][:60]}...")

    # Create test output directory
    TEST_OUTPUT_DIR.mkdir(exist_ok=True)
    test_folder = TEST_OUTPUT_DIR / "test_3"
    test_folder.mkdir(exist_ok=True)

    # Generate 3 images for test 3 using batches 7-9 (with nametags)
    print("\n" + "=" * 80)
    print("🎨 Generating Test 3 - 3 Images (750×750 square) WITH NAMETAGS")
    print("=" * 80)

    for image_num in range(1, 4):
        batch = batches[image_num + 5]  # Use batches 7, 8, 9

        print(f"\n📷 Image {image_num} - Using Batch {image_num + 6}:")
        for i, ep in enumerate(batch, 1):
            print(f"  {i}. {ep['podcast_name']}: {ep['title'][:60]}...")

        # Generate descriptions and extract participants for each episode
        print(f"  → Generating descriptions for {len(batch)} episodes...")
        episodes_with_descriptions = []
        for ep in batch:
            description = generate_episode_description(ep, anthropic_client)
            participants = extract_participants_from_summary(ep['summary_path'])
            episodes_with_descriptions.append({
                'title': ep['title'],
                'participants': participants,
                'description': description,
            })

        # Generate the image
        output_path = test_folder / f"test_3_picture_{image_num}.png"
        success = generate_composite_header_image(
            episodes_with_descriptions,
            3,
            image_num,
            output_path
        )

        if not success:
            print(f"  ⚠ Failed to generate Image {image_num}")

    print("\n" + "=" * 80)
    print(f"✓ Test 3 generation complete (WITH NAMETAGS)!")
    print(f"  Output directory: {test_folder}")
    print(f"  Generated: 3 images (750×750 square)")
    print(f"\n  Remaining batches available: {len(batches) - 9}")
    print("\nReview the images and provide feedback for iteration!")

if __name__ == "__main__":
    main()
