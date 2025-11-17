#!/usr/bin/env python3
"""
Generate OG image for Teahose - landscape format for social media previews
Based on user's provided design aesthetic
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Create the prompt based on the user's design
prompt = """
Create a photorealistic, sophisticated hero image for a tech podcast summary website called "Teahose".

COMPOSITION (Landscape 1536x1024 - PERFECTLY CENTERED):
- A beautifully lit cream-colored teacup filled with hot tea, CENTERED horizontally in the frame
- GENTLE STEAM visibly rising from the tea - subtle, elegant wisps of steam
- Teacup sitting on a matching saucer
- Single green tea leaf on the saucer as an elegant detail
- Warm, cozy background with subtle bokeh (blurred cafe/library setting) in the upper portion
- "Teahose" wordmark in modern SANS-SERIF font (clean, geometric, light weight like Helvetica or Inter), CENTERED below the cup in the lower third

CRITICAL COLOR REQUIREMENT FOR SURFACE/BACKGROUND:
- The bottom surface/table MUST be an extremely light, cool-toned cream color
- Think: barely off-white, like fresh eggshell or ivory paper
- RGB approximately (248, 247, 245) - almost white with the tiniest hint of warmth
- NOT tan, NOT beige, NOT warm sand color, NOT golden
- Similar to a clean white paper with just a whisper of cream
- The surface should look clean, minimal, and elegant - almost white

CENTERING REQUIREMENTS:
- Everything must be PERFECTLY CENTERED horizontally in the frame
- The teacup must be in the exact horizontal center
- The "Teahose" text must be centered below it

AESTHETIC:
- Photorealistic, high-end minimalist product photography
- Clean, bright lighting (not overly warm or golden)
- The background bokeh can be warm, but the surface/foreground must stay light and cool
- Dark brown/charcoal (#2c2c2c) for the wordmark in MODERN SANS-SERIF FONT
- Font style: Think Geist, Helvetica, Inter, or similar - clean, geometric, light weight
- Professional, sophisticated, calm atmosphere
- Shallow depth of field with teacup in focus
- Subtle steam rising from the hot tea

LIGHTING:
- Soft, bright natural light (think overcast day or softbox lighting)
- Avoid overly warm/golden tones on the surface
- The teacup can have warm tones from the tea inside
- Background can be warm and cozy
- But the surface the cup sits on should remain very light, cool, and clean

The surface color is KEY - it must be almost white, just barely cream. Like printing on off-white paper.
"""

print("Generating landscape OG image (1200x630) with photorealistic teacup aesthetic...")

response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    n=1,
    size="1536x1024",  # Landscape format (1.5:1 ratio)
    quality="high"
)

# Get the image URL or base64
image_data = response.data[0]

if hasattr(image_data, 'url') and image_data.url:
    # URL format
    import requests
    image_response = requests.get(image_data.url)
    image_bytes = image_response.content
elif hasattr(image_data, 'b64_json') and image_data.b64_json:
    # Base64 format
    image_bytes = base64.b64decode(image_data.b64_json)
else:
    raise ValueError("No image data returned")

# Save to temporary file first for preview
output_path = 'og-image-preview.png'
with open(output_path, 'wb') as f:
    f.write(image_bytes)

print(f"Preview image saved to {output_path}")
print("Please review before uploading to public/og-image.png")
