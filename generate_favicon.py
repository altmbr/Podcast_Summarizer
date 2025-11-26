#!/usr/bin/env python3
"""
Generate a favicon for Teahose using Google Gemini (Nano Banana Pro).
Creates favicon in multiple sizes for SEO and browser compatibility.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def generate_favicon():
    """Generate favicon using Nano Banana Pro."""
    try:
        from google import genai
    except ImportError:
        print("Installing google-genai...")
        import subprocess
        subprocess.run(["pip", "install", "-q", "google-genai"], check=True)
        from google import genai

    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY not set")
        return None

    # Prompt matching our comic design system
    prompt = """Create a square favicon/icon for "Teahose" - a tech podcast summary website.

CRITICAL SIZE REQUIREMENT:
- The teacup must fill 85-90% of the entire image
- VERY LARGE teacup taking up almost the whole square
- Minimal background visible - just a thin border around the cup
- NO small icons - make the cup HUGE

DESIGN:
- A single large stylized teacup with steam rising
- Teacup viewed from the side, filling the frame
- Simple steam wisps above the cup
- Vintage 1950s comic book / pop art style

COLOR PALETTE (must use these exact colors):
- Background: Warm cream (#f7f4f0)
- Teacup: Cardinal red (#c41e3a)
- Steam/accents: Golden yellow (#f4c430)
- Outline: Black (#1a1a1a) - thick bold lines (3-4px)

STYLE:
- Thick black outlines (comic book style)
- Ben Day halftone dots for shading on the cup
- High contrast, simple bold shapes
- Roy Lichtenstein pop art aesthetic
- Must be recognizable at 16x16px

OUTPUT:
- Square format (1:1 aspect ratio)
- NO text whatsoever
- Teacup fills the frame edge to edge"""

    try:
        client = genai.Client(api_key=google_api_key)
        
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=[prompt],
        )

        # Extract and save the generated image
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                
                # Save original
                output_path = Path("public/favicon-generated.png")
                image.save(str(output_path))
                print(f"✓ Favicon generated: {output_path}")
                
                return output_path

        print("⚠ No image data in response")
        return None

    except Exception as e:
        print(f"Error generating favicon: {e}")
        return None


def create_favicon_sizes(source_path):
    """Create multiple favicon sizes from source image."""
    try:
        from PIL import Image
    except ImportError:
        import subprocess
        subprocess.run(["pip", "install", "-q", "Pillow"], check=True)
        from PIL import Image

    if not source_path or not Path(source_path).exists():
        print("Source image not found")
        return

    img = Image.open(source_path)
    
    # Convert to RGBA if needed
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Make it square (crop center)
    width, height = img.size
    size = min(width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    img = img.crop((left, top, left + size, top + size))

    public_dir = Path("public")
    
    # Generate different sizes
    sizes = {
        'favicon-16x16.png': 16,
        'favicon-32x32.png': 32,
        'favicon-96x96.png': 96,
        'apple-touch-icon.png': 180,
        'favicon-512x512.png': 512,
    }

    for filename, size in sizes.items():
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(public_dir / filename, 'PNG')
        print(f"✓ Created {filename} ({size}x{size})")

    # Create .ico file (contains 16x16 and 32x32)
    img_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    img_16.save(public_dir / 'favicon.ico', format='ICO', sizes=[(16, 16), (32, 32)])
    print("✓ Created favicon.ico")

    print("\n✓ All favicon sizes generated!")
    print("  Files are in public/ directory")


if __name__ == "__main__":
    print("Generating favicon with Nano Banana Pro...")
    source = generate_favicon()
    if source:
        print("\nCreating favicon sizes...")
        create_favicon_sizes(source)
