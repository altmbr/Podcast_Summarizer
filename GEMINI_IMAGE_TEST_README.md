# Testing Google Imagen 3 for Weekly Summary Headers

This is a test setup to compare Google's Imagen 3 (via Gemini API) against OpenAI's GPT-image-1 for generating vintage newspaper-style comic headers for weekly podcast summaries.

## Setup

1. **Get a Google API Key:**
   - Visit https://aistudio.google.com/app/apikey
   - Create a new API key
   - Add it to your `.env` file:
     ```
     GOOGLE_API_KEY=your-key-here
     ```
   - Or use `GEMINI_API_KEY` instead (the script accepts both)

2. **Install Dependencies:**
   ```bash
   pip install google-generativeai
   ```
   ✅ Already installed!

## Usage

Run the test script on your latest pithy weekly summary:

```bash
python test_gemini_image_gen.py \
  --summary weekly_summaries/weekly_summary_2025-11-16_to_2025-11-23_pithy.md \
  --output weekly_summaries/weekly_summary_2025-11-16_to_2025-11-23_gemini_test.png
```

This will:
1. Extract the top 10 themes from your pithy summary
2. Generate a prompt for a 10-panel vintage newspaper-style comic header
3. Call Google's Imagen 3 API (`imagen-3.0-generate-001`)
4. Save the result as a PNG file

## Model Details

**Google Imagen 3:**
- Model ID: `imagen-3.0-generate-001`
- Aspect Ratio: 9:16 (portrait, mobile-friendly)
- Features: Latest Google image generation, optimized for photorealism and artistic styles
- Pricing: ~$0.04 per image (standard quality), ~$0.08 per image (high quality)

**Comparison to OpenAI GPT-image-1:**
- Both support similar quality levels
- Imagen 3 may excel at certain artistic styles
- Cost is comparable (~$0.04-0.08 per image)

## Next Steps

After testing:
1. Compare the Gemini-generated image to the OpenAI-generated version
2. If Gemini produces better results, we can:
   - Update `generate_weekly_header_image.py` to use Gemini instead
   - Or add a `--model` flag to choose between OpenAI and Gemini
3. The existing weekly summary generation will remain unchanged for now

## Notes

- The test script (`test_gemini_image_gen.py`) is separate from the production script
- No changes to your existing workflow until you decide
- Both APIs support similar prompt styles and requirements
