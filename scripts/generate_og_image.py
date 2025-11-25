#!/usr/bin/env python3
"""
Generate a clean, brand-aligned OG image for Teahose.
Style: Elegant typography on cream background with charcoal text.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Brand colors
CREAM = (248, 247, 245)      # #f8f7f5
CHARCOAL = (44, 44, 44)      # #2c2c2c
SLATE_BLUE = (91, 127, 158)  # #5b7f9e
MUTED = (90, 90, 90)         # #5a5a5a

# OG image dimensions (1200x630 is standard for social)
WIDTH = 1200
HEIGHT = 630

def generate_og_image(output_path: Path):
    """Generate a clean, typography-first OG image."""

    # Create image with cream background
    img = Image.new('RGB', (WIDTH, HEIGHT), CREAM)
    draw = ImageDraw.Draw(img)

    # Try to load system fonts, fall back to default
    try:
        # Try common system font paths
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/SFNSDisplay.ttf",
            "/Library/Fonts/Arial.ttf",
        ]
        title_font = None
        for fp in font_paths:
            if Path(fp).exists():
                title_font = ImageFont.truetype(fp, 120)
                tagline_font = ImageFont.truetype(fp, 32)
                break
        if not title_font:
            title_font = ImageFont.load_default()
            tagline_font = ImageFont.load_default()
    except Exception:
        title_font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()

    # Draw subtle accent line at top
    draw.rectangle([(0, 0), (WIDTH, 6)], fill=SLATE_BLUE)

    # Main title: "Teahose"
    title = "Teahose"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (WIDTH - title_width) // 2
    title_y = HEIGHT // 2 - 80
    draw.text((title_x, title_y), title, font=title_font, fill=CHARCOAL)

    # Tagline
    tagline = "Tech Podcast Summaries"
    tagline_bbox = draw.textbbox((0, 0), tagline, font=tagline_font)
    tagline_width = tagline_bbox[2] - tagline_bbox[0]
    tagline_x = (WIDTH - tagline_width) // 2
    tagline_y = title_y + 130
    draw.text((tagline_x, tagline_y), tagline, font=tagline_font, fill=MUTED)

    # Subtle decorative elements - small dots
    dot_y = tagline_y + 60
    dot_spacing = 20
    dot_start_x = WIDTH // 2 - (2 * dot_spacing)
    for i in range(5):
        x = dot_start_x + (i * dot_spacing)
        draw.ellipse([(x-2, dot_y-2), (x+2, dot_y+2)], fill=SLATE_BLUE)

    # Save
    img.save(output_path, 'PNG', optimize=True)
    print(f"Generated OG image: {output_path}")

if __name__ == "__main__":
    output = Path(__file__).parent.parent / "public" / "og-image-new.png"
    generate_og_image(output)
    print(f"\nTo use this image, rename it to og-image.png")
