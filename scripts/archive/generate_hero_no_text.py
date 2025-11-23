#!/usr/bin/env python3
"""
Generate hero image without text - just the teacup with steam
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

prompt = """
Create a photorealistic, sophisticated hero image of a teacup.

COMPOSITION (Landscape 1536x1024 - PERFECTLY CENTERED):
- A beautifully lit cream-colored teacup filled with hot tea, CENTERED horizontally in the frame
- GENTLE STEAM visibly rising from the tea - subtle, elegant wisps of steam
- Teacup sitting on a matching saucer
- Single green tea leaf on the saucer as an elegant detail
- Warm, cozy background with subtle bokeh (blurred cafe/library setting) in the upper portion
- NO TEXT - just the teacup and background

CRITICAL COLOR REQUIREMENT FOR SURFACE/BACKGROUND:
- The bottom surface/table MUST be an extremely light, cool-toned cream color
- Think: barely off-white, like fresh eggshell or ivory paper
- RGB approximately (248, 247, 245) - almost white with the tiniest hint of warmth
- NOT tan, NOT beige, NOT warm sand color, NOT golden
- Similar to a clean white paper with just a whisper of cream
- The surface should look clean, minimal, and elegant - almost white

CENTERING REQUIREMENTS:
- The teacup must be in the exact horizontal center of the frame

AESTHETIC:
- Photorealistic, high-end minimalist product photography
- Clean, bright lighting (not overly warm or golden)
- The background bokeh can be warm, but the surface/foreground must stay light and cool
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
NO TEXT OR WORDMARK - this is purely a product photograph of a teacup.
"""

print("Generating hero image without text...")

response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    n=1,
    size="1536x1024",
    quality="high"
)

# Get the image data
image_data = response.data[0]

if hasattr(image_data, 'url') and image_data.url:
    import requests
    image_response = requests.get(image_data.url)
    image_bytes = image_response.content
elif hasattr(image_data, 'b64_json') and image_data.b64_json:
    image_bytes = base64.b64decode(image_data.b64_json)
else:
    raise ValueError("No image data returned")

# Save to file
output_path = 'hero-no-text.png'
with open(output_path, 'wb') as f:
    f.write(image_bytes)

print(f"Hero image (no text) saved to {output_path}")
