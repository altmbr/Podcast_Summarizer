#!/usr/bin/env python3
"""
Generate Open Graph / Twitter Card image for teahose.com social media sharing.
Matches the site's elegant cream and charcoal aesthetic.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def generate_og_image():
    """Generate social media preview image for teahose.com"""

    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Design prompt matching the site's aesthetic
    prompt = """
    Create a minimalist, elegant social media preview image (landscape orientation) for a podcast summary website called "Teahose".

    Style requirements:
    - Background: elegant cream color (#f8f7f5)
    - Text color: charcoal (#2c2c2c)
    - Accent color: muted dusty blue (#5b7f9e)
    - Typography: clean, modern sans-serif, light weight
    - Overall aesthetic: sophisticated, minimalist, content-focused

    Layout (horizontal/landscape):
    - Center-aligned composition optimized for landscape format
    - Large "Teahose" title in charcoal at center
    - Below it: "Thoughtful podcast summaries & transcripts" in smaller, lighter text
    - Include a subtle visual element: perhaps a minimalist teacup icon or abstract podcast microphone/wave pattern in the muted blue accent color
    - Bottom area: "Explore, learn, and reflect on compelling ideas" in very light charcoal

    The design should feel:
    - Intellectual and curated
    - Clean and uncluttered
    - Professional yet approachable
    - Like a high-end content platform
    - Optimized for social media sharing (Facebook, Twitter, LinkedIn)

    Landscape orientation for optimal social media display.
    """

    print("Generating Open Graph image for teahose.com...")
    print("This will use OpenAI's image generation API (gpt-image-1)")

    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            n=1,
            size="1536x1024",  # Landscape format, closest to 1200x630 OG standard
            quality="high"
        )

        # Handle both URL and base64 responses
        import base64

        if hasattr(response.data[0], 'b64_json') and response.data[0].b64_json:
            # Base64 response
            print(f"\n✅ Image generated successfully (base64 format)!")
            image_data = base64.b64decode(response.data[0].b64_json)
        elif hasattr(response.data[0], 'url') and response.data[0].url:
            # URL response
            print(f"\n✅ Image generated successfully!")
            print(f"Image URL: {response.data[0].url}")
            import requests
            image_data = requests.get(response.data[0].url).content
        else:
            raise Exception("Unexpected response format from OpenAI API")

        output_path = os.path.join(os.path.dirname(__file__), 'public', 'og-image.png')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'wb') as f:
            f.write(image_data)

        print(f"💾 Image saved to: {output_path}")
        print(f"📏 Image size: 1536x1024 (landscape, close to optimal 1200x630 OG size)")
        print("\nNext steps:")
        print("1. Review the image to ensure it matches the brand aesthetic")
        print("2. If needed, regenerate with adjusted prompt")
        print("3. Add Open Graph meta tags to app/layout.tsx")

        return output_path

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None

if __name__ == "__main__":
    generate_og_image()
