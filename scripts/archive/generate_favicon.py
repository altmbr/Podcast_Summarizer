#!/usr/bin/env python3
"""
Generate favicon (teacup icon) for teahose.com.
Matches the style from the OG image.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def generate_favicon():
    """Generate teacup favicon matching the OG image style"""

    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Design prompt for teacup icon
    prompt = """
    Create a minimalist teacup icon for a website favicon.

    Style requirements:
    - Simple, elegant teacup silhouette in muted dusty blue (#5b7f9e)
    - The teacup should FILL THE CANVAS - zoom in close so the cup takes up 70-80% of the square
    - Very minimal negative space around the edges
    - Clean, bold design that reads well at tiny sizes (16x16px)
    - Light steam wisps rising from the cup (optional, keep subtle)
    - Light cream or white background (#f8f7f5)
    - IMPORTANT: The teacup should be LARGE and prominent, not small and centered with lots of white space

    The design should:
    - Fill most of the canvas with the teacup shape
    - Be immediately recognizable even at 16x16 pixels
    - Have bold, clear edges
    - Match the sophisticated, minimal aesthetic
    - Be cropped close to the teacup (think tight crop, not lots of padding)

    Think: emoji-sized icon where the teacup fills the square, not a tiny icon with lots of empty space.
    """

    print("Generating favicon (teacup icon) for teahose.com...")
    print("This will use OpenAI's image generation API (gpt-image-1)")

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            n=1,
            size="1024x1024",  # Square format for favicon
            quality="high"
        )

        # Handle base64 response
        import base64

        if hasattr(response.data[0], 'b64_json') and response.data[0].b64_json:
            print(f"\n✅ Favicon generated successfully!")
            image_data = base64.b64decode(response.data[0].b64_json)
        elif hasattr(response.data[0], 'url') and response.data[0].url:
            print(f"\n✅ Favicon generated successfully!")
            import requests
            image_data = requests.get(response.data[0].url).content
        else:
            raise Exception("Unexpected response format from OpenAI API")

        # Save to app directory (Next.js 13+ convention)
        output_path = os.path.join(os.path.dirname(__file__), 'app', 'favicon.ico')

        with open(output_path, 'wb') as f:
            f.write(image_data)

        print(f"💾 Favicon saved to: {output_path}")
        print(f"📏 Image size: 1024x1024 (will be automatically resized by browsers)")
        print("\n✨ Favicon is ready! Next.js will automatically detect it in the app directory.")

        return output_path

    except Exception as e:
        print(f"❌ Error generating favicon: {e}")
        return None

if __name__ == "__main__":
    generate_favicon()
