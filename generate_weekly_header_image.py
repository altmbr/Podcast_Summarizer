#!/usr/bin/env python3
"""
Generate newspaper-style comic header images for weekly podcast summaries.

This script creates vintage newspaper-style header images with 6 panels
displaying the key themes from the weekly podcast summary.

Usage:
    python generate_weekly_header_image.py --date 2025-11-04_to_2025-11-11
    python generate_weekly_header_image.py --themes "Theme 1" "Theme 2" ... --output header.png
"""

import os
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Image generation settings
IMAGE_MODEL = "gpt-image-1"  # OpenAI's latest GPT-4o native image generation
IMAGE_SIZE = "1024x1536"  # Portrait orientation for mobile-friendly viewing (options: 1024x1024, 1024x1536, 1536x1024, auto)
IMAGE_QUALITY = "high"  # Use high quality for better detail (options: low, medium, high, auto)
NUM_PANELS = 10  # Number of comic panels (5 rows x 2 columns for portrait)


def extract_themes_from_summary(summary_file_path, num_panels=NUM_PANELS):
    """
    Extract key themes and contrarian insights from a weekly summary markdown file.
    Handles both pithy format (##) and regular format (**).

    Args:
        summary_file_path: Path to the weekly summary markdown file
        num_panels: Number of panels to extract (default: 10)

    Returns:
        list: List of up to num_panels panel titles combining themes and insights
    """
    try:
        with open(summary_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        all_panels = []

        # Try pithy format first: ## A. Key Topics with ### N. Topic Name
        key_topics_match = re.search(r'## A\. Key Topics(.*?)(?=## [A-Z]\.|\Z)', content, re.DOTALL)
        if key_topics_match:
            topics_text = key_topics_match.group(1)
            # Extract topic titles from ### N. Topic Name
            topic_matches = re.findall(r'###\s+\d+\.\s+(.+)', topics_text)
            all_panels.extend([t.strip() for t in topic_matches])

        # Try regular format: **A. Topics Discussed** with N. **Topic Name**
        if not all_panels:
            topics_match = re.search(r'\*\*A\. Topics? Discussed\*\*(.*?)(?=\*\*[A-Z]\.|\Z)', content, re.DOTALL)
            if topics_match:
                topics_text = topics_match.group(1)
                # Extract topic titles from N. **Topic Name**
                topic_matches = re.findall(r'^\d+\.\s+\*\*([^*]+)\*\*', topics_text, re.MULTILINE)
                all_panels.extend([t.strip() for t in topic_matches])

        # Extract Contrarian Perspectives
        # Try pithy format: ## B. Contrarian Perspectives
        contrarian_match = re.search(r'## B\. Contrarian Perspectives(.*?)(?=## [A-Z]\.|\Z)', content, re.DOTALL)
        if contrarian_match:
            contrarian_text = contrarian_match.group(1)
            # Extract contrarian titles from **Title** format
            contrarian_matches = re.findall(r'\*\*([^*]+)\*\*', contrarian_text)
            # Filter out quotes and long text (only keep short titles)
            contrarian_titles = [c.strip() for c in contrarian_matches
                               if len(c.strip()) > 10 and len(c.strip()) < 80
                               and not c.strip().startswith('->')]
            all_panels.extend(contrarian_titles)
        else:
            # Try regular format: **B. Contrarian Perspectives**
            contrarian_match = re.search(r'\*\*B\. Contrarian Perspectives\*\*(.*?)(?=\*\*[A-Z]\.|\Z)', content, re.DOTALL)
            if contrarian_match:
                contrarian_text = contrarian_match.group(1)
                # Extract from N. **Perspective Title**
                contrarian_matches = re.findall(r'^\d+\.\s+\*\*([^*]+)\*\*', contrarian_text, re.MULTILINE)
                all_panels.extend([c.strip() for c in contrarian_matches if len(c.strip()) > 10])

        # Return first num_panels
        result = all_panels[:num_panels]

        print(f"Extracted {len(result)} panel titles from summary")
        for i, panel in enumerate(result, 1):
            print(f"  {i}. {panel}")

        return result

    except Exception as e:
        print(f"Error extracting themes from summary: {e}")
        import traceback
        traceback.print_exc()
        return []


def create_image_prompt(panel_titles, date_str):
    """
    Create a detailed prompt for generating the newspaper-style comic header.

    Args:
        panel_titles: List of 10 panel titles/themes
        date_str: Date string for the newspaper header (e.g., "SUNDAY, NOVEMBER 16, 2025")

    Returns:
        str: Detailed prompt for image generation
    """
    # Ensure we have exactly 10 panels
    if len(panel_titles) < NUM_PANELS:
        panel_titles = panel_titles + [""] * (NUM_PANELS - len(panel_titles))
    panel_titles = panel_titles[:NUM_PANELS]

    # Format panel titles for the prompt
    panel_list = "\n".join([f"{i+1}. {title}" for i, title in enumerate(panel_titles) if title])

    prompt = f"""Create a vintage newspaper-style comic header in the exact style of a 1950s newspaper comic section.

CRITICAL LAYOUT REQUIREMENTS:
- Title at top: "PODCAST WEEKLY DIGEST" in bold serif newspaper font (keep compact)
- Subtitle: "{date_str}" (keep compact)
- EXACTLY 10 comic panels arranged in a 5x2 grid below the title (5 rows, 2 columns)
- ALL 10 PANELS MUST BE FULLY VISIBLE - do not cut off any panels at the bottom
- Each panel has a title header in ALL CAPS above the artwork
- Panels should be equal-sized and fit completely within the image bounds
- Portrait orientation (1024x1536 pixels)
- Leave NO empty space at top - maximize space for the 10 panels
- Ensure the entire 5x2 grid fits within the image height

ARTISTIC STYLE - Vintage 1950s Roy Lichtenstein pop art:
- BACKGROUND: Warm aged cream paper (#f7f4f0) with subtle halftone dot texture
- BORDERS: Thick black outlines (3px) around all panels and main border
- COLORS: Bold pop art accents - cardinal red (#c41e3a), golden yellow (#f4c430), deep blue (#2d5a7b)
- SHADOWS: Black comic drop shadows (not brown)
- TEXTURE: Ben Day halftone dots for shading, stipple patterns
- OVERALL: Clean vintage newspaper comic with warm cream base + bold accent colors

PANEL TITLES AND THEMES:
{panel_list}

PANEL CONTENT REQUIREMENTS:
Each panel should contain:
- Relevant symbolic imagery representing the theme
- Human figures in vintage comic book style when appropriate with halftone shading
- Visual metaphors and symbols (brains for AI, scales for justice, money symbols, etc.)
- Dynamic compositions with visual interest
- No text beyond the UPPERCASE panel titles
- Simple, iconic imagery that reads well at small sizes
- Thick black outlines around all elements

COLOR SCHEME:
- Overall background: warm cream aged paper (#f7f4f0)
- Panel backgrounds rotate between: soft red tint (#fdf5f5), soft yellow tint (#fffcf0), soft blue tint (#f5f8fa), cream (#f5f0e8)
- Bold accent colors for main elements: cardinal red, golden yellow, deep blue
- Thick black borders and outlines (3px)
- Black comic drop shadows on panels
- Ben Day dot patterns for shading

OVERALL AESTHETIC:
- Clean, professional newspaper comic section appearance
- Warm cream aged paper base with bold pop art accents
- Nostalgic 1950s-60s mid-century modern design
- Educational and thought-provoking imagery
- Sophisticated but accessible visual metaphors
- Print-ready quality with sharp lines and clear composition
- Mobile-friendly portrait format perfect for email and newsletters"""

    return prompt


def generate_header_image(panel_titles, date_str, output_path, reference_image_path=None):
    """
    Generate the newspaper-style header image using OpenAI's image generation API.

    Args:
        panel_titles: List of 6 panel titles/themes
        date_str: Date string for the header
        output_path: Where to save the generated image
        reference_image_path: Optional path to reference image for style matching

    Returns:
        str: Path to the generated image
    """
    print(f"Generating header image with {len(panel_titles)} themes...")
    print(f"Using model: {IMAGE_MODEL}")

    # Create the prompt
    prompt = create_image_prompt(panel_titles, date_str)

    print("\nGenerated prompt:")
    print("-" * 80)
    print(prompt)
    print("-" * 80)

    try:
        # Generate the image
        print(f"\nCalling OpenAI API to generate image...")
        response = client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            size=IMAGE_SIZE,
            quality=IMAGE_QUALITY,
            n=1
        )

        # Get the image URL or base64 data
        if hasattr(response.data[0], 'url') and response.data[0].url:
            # Download from URL
            import urllib.request
            image_url = response.data[0].url
            print(f"Downloading image from: {image_url}")
            urllib.request.urlretrieve(image_url, output_path)
        elif hasattr(response.data[0], 'b64_json') and response.data[0].b64_json:
            # Save base64 data
            print("Saving base64 encoded image...")
            image_data = base64.b64decode(response.data[0].b64_json)
            with open(output_path, 'wb') as f:
                f.write(image_data)
        else:
            raise ValueError("No image data returned from API")

        print(f"\n✓ Image saved to: {output_path}")
        return output_path

    except Exception as e:
        print(f"\n✗ Error generating image: {e}")
        raise


def format_date_string(date_range_str=None):
    """
    Format a date string for the newspaper header.

    Args:
        date_range_str: Optional date range string like "2025-11-04_to_2025-11-11"

    Returns:
        str: Formatted date like "SUNDAY, NOVEMBER 16, 2025"
    """
    if date_range_str:
        # Extract the end date from the range
        try:
            end_date_str = date_range_str.split('_to_')[-1]
            date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
            return date_obj.strftime('%A, %B %d, %Y').upper()
        except:
            pass

    # Default to today's date
    return datetime.now().strftime('%A, %B %d, %Y').upper()


def main():
    parser = argparse.ArgumentParser(
        description='Generate newspaper-style comic header for weekly podcast summaries'
    )
    parser.add_argument(
        '--date',
        help='Date range string (e.g., "2025-11-04_to_2025-11-11")'
    )
    parser.add_argument(
        '--summary',
        help='Path to weekly summary markdown file to extract themes from'
    )
    parser.add_argument(
        '--themes',
        nargs='+',
        help='List of 6 panel themes/titles (if not using --summary)'
    )
    parser.add_argument(
        '--output',
        default='weekly_header.png',
        help='Output path for generated image (default: weekly_header.png)'
    )
    parser.add_argument(
        '--reference',
        help='Path to reference image for style matching (optional)'
    )

    args = parser.parse_args()

    # Validate API key
    if not os.getenv('OPENAI_API_KEY'):
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please add it to your .env file")
        sys.exit(1)

    # Get panel titles
    panel_titles = []

    if args.summary:
        # Extract from summary file
        print(f"Extracting themes from: {args.summary}")
        panel_titles = extract_themes_from_summary(args.summary)
        if not panel_titles:
            print("Warning: Could not extract themes from summary file")

    if args.themes:
        # Use provided themes
        panel_titles = args.themes[:6]

    if not panel_titles:
        print("Error: No themes provided. Use --summary or --themes")
        print("\nExample usage:")
        print("  python generate_weekly_header_image.py --summary weekly_summaries/summary.md")
        print("  python generate_weekly_header_image.py --themes 'AI Development' 'Media Industry' ...")
        sys.exit(1)

    # Ensure we have at least 6 themes
    if len(panel_titles) < 6:
        print(f"Warning: Only {len(panel_titles)} themes provided, need 6 panels")
        print("Remaining panels will be left empty")

    # Format the date
    date_str = format_date_string(args.date)
    print(f"\nGenerating header for: {date_str}")
    print(f"Panel themes: {panel_titles}")

    # Generate the image
    try:
        output_path = generate_header_image(
            panel_titles,
            date_str,
            args.output,
            args.reference
        )
        print(f"\n✓ Successfully generated header image!")
        print(f"  Output: {output_path}")
    except Exception as e:
        print(f"\n✗ Failed to generate image: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
