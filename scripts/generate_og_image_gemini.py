#!/usr/bin/env python3
"""
Generate a vintage comic-style OG image using Google Gemini (Nano Banana Pro).
Similar to daily email headers but for social preview.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def generate_og_image():
    """Generate OG image using Gemini."""
    try:
        from google import genai
    except ImportError:
        print("Installing google-genai...")
        import subprocess
        subprocess.run(["pip", "install", "-q", "google-genai"], check=True)
        from google import genai

    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY not set in .env")
        return None

    # Prompt for vintage comic-style OG image
    # OG images are landscape 1200x630, unlike the portrait email headers
    prompt = """Create a vintage 1950s newspaper-style comic header for "Teahose - Tech Podcast Summaries".

LAYOUT: Single wide panel in LANDSCAPE format (wider than tall).

STYLE: Vintage Roy Lichtenstein pop art with Ben Day dots, bold primary colors, thick black outlines.

SCENE: A retro 1950s business scene showing people having thoughtful conversations over tea/coffee. Include speech bubbles with tech/business themes like "AI", "Startups", "Innovation". Make it look like a vintage newspaper comic strip header.

TEXT: Bold "TEAHOSE" text prominently displayed at the top or integrated into the scene. Subtitle "Tech Podcast Summaries" in smaller vintage newspaper font.

REQUIREMENTS:
- Landscape orientation (1200x630 pixels, wider than tall)
- Vintage newspaper comic aesthetic with Ben Day dots
- Bold, legible text
- Retro 1950s color palette (reds, blues, yellows, with cream/beige background tones)
- Professional yet playful tone
- All text clearly readable"""

    try:
        print("Generating OG image with Gemini (Nano Banana Pro)...")
        client = genai.Client(api_key=google_api_key)

        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        # Extract and save the generated image
        output_path = Path(__file__).parent.parent / "public" / "og-image.png"

        from PIL import Image as PILImage

        for part in response.parts:
            if part.inline_data is not None:
                # The part.as_image() returns a PIL Image object
                img = part.as_image()

                # Save directly - Gemini should generate at correct size
                img.save(str(output_path))
                print(f"OG image generated: {output_path}")
                print(f"Image size: {img.size}")
                return output_path

        print("Warning: No image data in response")
        return None
    except Exception as e:
        print(f"Error generating OG image: {e}")
        return None


if __name__ == "__main__":
    generate_og_image()
