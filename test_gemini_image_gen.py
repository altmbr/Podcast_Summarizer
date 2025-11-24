#!/usr/bin/env python3
"""
Test script for generating header images using Google's Imagen 3 (via Gemini API).

Usage:
    python test_gemini_image_gen.py --summary weekly_summaries/weekly_summary_2025-11-16_to_2025-11-23_pithy.md
"""

import os
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Image generation settings
IMAGE_MODEL = "imagen-3.0-generate-001"  # Google's latest Imagen 3 model
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
        # But the actual format is: **A. Topics Discussed** with N. **Topic Name**
        topics_match = re.search(r'\*\*A\. Topics? Discussed\*\*(.*?)(?=\*\*[A-Z]\.|\Z)', content, re.DOTALL)
        if topics_match:
            topics_text = topics_match.group(1)
            # Extract topic titles from N. **Topic Name**
            topic_matches = re.findall(r'^\d+\.\s+\*\*([^*]+)\*\*', topics_text, re.MULTILINE)
            all_panels.extend([t.strip() for t in topic_matches])

        # Extract Contrarian Perspectives
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
- Portrait orientation (9:16 aspect ratio, vertical format)
- Leave NO empty space at top - maximize space for the 10 panels
- Ensure the entire 5x2 grid fits within the image height

ARTISTIC STYLE:
- Vintage 1950s-1960s comic book art style
- Bold, simple line art with thick black outlines
- Ben Day dots and halftone shading patterns
- Limited color palette: primarily yellow, red, blue, and beige/cream backgrounds
- Roy Lichtenstein pop art aesthetic
- High contrast, flat colors
- Clean grid layout with equal-sized rectangular panels

PANEL TITLES AND THEMES:
{panel_list}

PANEL CONTENT REQUIREMENTS:
Each panel should contain:
- Relevant symbolic imagery representing the theme
- Human figures in vintage comic book style when appropriate
- Visual metaphors and symbols (brains for AI, scales for justice, money symbols, etc.)
- Dynamic compositions with visual interest
- No text beyond the panel titles
- Simple, iconic imagery that reads well at small sizes

COLOR SCHEME:
- Panel backgrounds should alternate between: bright yellow, red, blue, and cream
- Use bold, saturated colors
- Black outlines and details
- White highlights and Ben Day dot patterns for shading
- Maintain visual variety across all 10 panels

OVERALL AESTHETIC:
- Clean, professional newspaper comic section appearance
- Nostalgic 1950s-60s mid-century modern design
- Educational and thought-provoking imagery
- Sophisticated but accessible visual metaphors
- Print-ready quality with sharp lines and clear composition
- Mobile-friendly portrait format perfect for email and newsletters"""

    return prompt


def generate_header_image_gemini(panel_titles, date_str, output_path):
    """
    Generate the newspaper-style header image using Google's Imagen 3.

    Args:
        panel_titles: List of 10 panel titles/themes
        date_str: Date string for the header
        output_path: Where to save the generated image

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
        # Configure the API
        api_key = os.getenv('GOOGLE_API_KEY') or os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_API_KEY or GEMINI_API_KEY not found in environment variables")

        genai.configure(api_key=api_key)

        # Generate the image
        print(f"\nCalling Google Gemini API to generate image...")

        # Using the Imagen model via genai
        model = genai.GenerativeModel(IMAGE_MODEL)

        # Generate image with portrait aspect ratio (9:16)
        response = model.generate_images(
            prompt=prompt,
            number_of_images=1,
            aspect_ratio="9:16",  # Portrait orientation for mobile-friendly viewing
            safety_filter_level="block_only_high",  # Allow creative content
            person_generation="allow_adult"  # Allow human figures in vintage style
        )

        # Save the generated image
        if response.images:
            image = response.images[0]

            # Save to file
            print(f"Saving image to: {output_path}")
            with open(output_path, 'wb') as f:
                f.write(image._pil_image.tobytes())

            # Alternative: if the above doesn't work, try this
            try:
                image._pil_image.save(output_path)
            except:
                # If PIL save fails, try getting raw bytes
                image_data = image._image_bytes
                with open(output_path, 'wb') as f:
                    f.write(image_data)

            print(f"\n✓ Image saved to: {output_path}")
            return output_path
        else:
            raise ValueError("No images returned from API")

    except Exception as e:
        print(f"\n✗ Error generating image: {e}")
        import traceback
        traceback.print_exc()
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
        description='Test generating newspaper-style comic header using Google Imagen 3'
    )
    parser.add_argument(
        '--date',
        help='Date range string (e.g., "2025-11-16_to_2025-11-23")'
    )
    parser.add_argument(
        '--summary',
        help='Path to weekly summary markdown file to extract themes from'
    )
    parser.add_argument(
        '--themes',
        nargs='+',
        help='List of 10 panel themes/titles (if not using --summary)'
    )
    parser.add_argument(
        '--output',
        default='weekly_header_gemini_test.png',
        help='Output path for generated image (default: weekly_header_gemini_test.png)'
    )

    args = parser.parse_args()

    # Validate API key
    api_key = os.getenv('GOOGLE_API_KEY') or os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GOOGLE_API_KEY or GEMINI_API_KEY not found in environment variables")
        print("Please add one of them to your .env file")
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
        panel_titles = args.themes[:10]

    if not panel_titles:
        print("Error: No themes provided. Use --summary or --themes")
        print("\nExample usage:")
        print("  python test_gemini_image_gen.py --summary weekly_summaries/weekly_summary_2025-11-16_to_2025-11-23_pithy.md")
        print("  python test_gemini_image_gen.py --themes 'AI Development' 'Media Industry' ...")
        sys.exit(1)

    # Ensure we have at least 10 themes
    if len(panel_titles) < 10:
        print(f"Warning: Only {len(panel_titles)} themes provided, need 10 panels")
        print("Remaining panels will be left empty")

    # Format the date (extract from summary filename if available)
    date_str = args.date
    if not date_str and args.summary:
        # Try to extract date from filename
        match = re.search(r'(\d{4}-\d{2}-\d{2}_to_\d{4}-\d{2}-\d{2})', args.summary)
        if match:
            date_str = match.group(1)

    date_str = format_date_string(date_str)
    print(f"\nGenerating header for: {date_str}")
    print(f"Panel themes: {panel_titles}")

    # Generate the image
    try:
        output_path = generate_header_image_gemini(
            panel_titles,
            date_str,
            args.output
        )
        print(f"\n✓ Successfully generated header image!")
        print(f"  Output: {output_path}")
    except Exception as e:
        print(f"\n✗ Failed to generate image: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
