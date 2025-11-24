#!/usr/bin/env python3
"""
Generate a pithy/condensed version of the most recent weekly summary.
Takes the full weekly summary and condenses it while preserving quotes.
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
WEEKLY_SUMMARIES_DIR = Path("./weekly_summaries")
PITHY_PROMPT_FILE = Path("./pithy_weekly_summary_prompt.md")
CLAUDE_MODEL = "claude-sonnet-4-5-20250929"

# Default prompt if file doesn't exist
DEFAULT_PITHY_PROMPT = """Condense this weekly summary to be more concise and scannable while keeping all quotes exactly as written. Remove less critical content, but preserve the most valuable insights. Aim for 40-60% of the original length."""

def load_pithy_prompt():
    """Load the pithy summary prompt from file or use default"""
    if PITHY_PROMPT_FILE.exists():
        content = PITHY_PROMPT_FILE.read_text().strip()
        if content:
            return content

    print(f"⚠ Note: Using default pithy prompt")
    print(f"   You can customize by editing: {PITHY_PROMPT_FILE}")
    return DEFAULT_PITHY_PROMPT

def find_most_recent_weekly_summary():
    """Find the most recent weekly summary file"""
    if not WEEKLY_SUMMARIES_DIR.exists():
        print(f"❌ Error: {WEEKLY_SUMMARIES_DIR} directory not found")
        print("   Run generate_weekly_summary.py first")
        sys.exit(1)

    # Find all weekly_summary_*.md files (excluding _pithy versions)
    summary_files = [
        f for f in WEEKLY_SUMMARIES_DIR.glob("weekly_summary_*.md")
        if "_pithy" not in f.name
    ]

    if not summary_files:
        print(f"❌ Error: No weekly summary files found in {WEEKLY_SUMMARIES_DIR}")
        print("   Run generate_weekly_summary.py first")
        sys.exit(1)

    # Sort by modification time (most recent first)
    summary_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return summary_files[0]

def generate_pithy_summary(full_summary_content, pithy_prompt):
    """Generate a pithy version using Claude"""
    print(f"  → Generating pithy version with AI...")

    try:
        from anthropic import Anthropic
    except ImportError:
        print("❌ Error: Anthropic SDK not installed")
        print("   Install with: pip install anthropic")
        sys.exit(1)

    anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not anthropic_api_key:
        print("❌ Error: ANTHROPIC_API_KEY not set in .env file")
        sys.exit(1)

    # Build the full prompt
    full_prompt = f"""{pithy_prompt}

---

# FULL WEEKLY SUMMARY TO CONDENSE

{full_summary_content}
"""

    # Call Claude API
    client = Anthropic(api_key=anthropic_api_key)

    print(f"  → Input size: {len(full_summary_content):,} characters")

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=16000,  # Increased from 8000 to match full weekly summary capacity
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    pithy_summary = response.content[0].text
    print(f"  ✓ Pithy summary generated ({len(pithy_summary):,} characters)")

    # Calculate reduction
    reduction_pct = (1 - len(pithy_summary) / len(full_summary_content)) * 100
    print(f"  → Reduced by {reduction_pct:.1f}%")

    return pithy_summary

def save_pithy_summary(pithy_content, original_path):
    """Save the pithy summary with _pithy suffix"""
    # Generate filename by adding _pithy before .md
    pithy_filename = original_path.stem + "_pithy.md"
    pithy_path = original_path.parent / pithy_filename

    with open(pithy_path, 'w') as f:
        f.write(pithy_content)

    # Also generate HTML version
    print("→ Generating HTML version for email...")
    html_filename = original_path.stem + "_pithy.html"
    html_path = original_path.parent / html_filename

    # Import the HTML generation function from generate_weekly_summary
    from generate_weekly_summary import generate_html_version
    from datetime import datetime

    # Extract date range from filename (format: weekly_summary_YYYY-MM-DD_to_YYYY-MM-DD.md)
    import re
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})_to_(\d{4}-\d{2}-\d{2})', original_path.stem)
    if date_match:
        start_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
        end_date = datetime.strptime(date_match.group(2), '%Y-%m-%d')

        # Check if header image exists
        image_filename = original_path.stem + "_header.png"
        image_path = original_path.parent / image_filename
        image_name = image_filename if image_path.exists() else None

        # Generate HTML
        generate_html_version(pithy_path, html_path, [], start_date, end_date, image_name)
        print(f"  ✓ HTML version saved to: {html_path}")

    return pithy_path

def main():
    print(f"\n{'='*70}")
    print(f"📝 PITHY WEEKLY SUMMARY GENERATOR")
    print(f"{'='*70}\n")

    # Load pithy prompt
    print("→ Loading pithy summary prompt...")
    pithy_prompt = load_pithy_prompt()
    print("  ✓ Prompt loaded")

    # Find most recent weekly summary
    print("\n→ Finding most recent weekly summary...")
    summary_path = find_most_recent_weekly_summary()
    print(f"  ✓ Found: {summary_path.name}")

    # Read the full summary
    print("\n→ Reading full weekly summary...")
    with open(summary_path, 'r', encoding='utf-8') as f:
        full_summary = f.read()
    print(f"  ✓ Loaded ({len(full_summary):,} characters)")

    # Generate pithy version
    print(f"\n{'='*70}")
    print("Generating pithy version...")
    print(f"{'='*70}\n")

    pithy_summary = generate_pithy_summary(full_summary, pithy_prompt)

    if not pithy_summary:
        print("❌ Failed to generate pithy summary")
        sys.exit(1)

    # Save pithy summary
    print("\n→ Saving pithy summary...")
    output_path = save_pithy_summary(pithy_summary, summary_path)

    print(f"\n{'='*70}")
    print(f"✅ PITHY SUMMARY COMPLETE")
    print(f"{'='*70}")
    print(f"\n📄 Pithy summary saved to: {output_path}")
    print(f"   Original: {len(full_summary):,} characters")
    print(f"   Pithy: {len(pithy_summary):,} characters")

    reduction_pct = (1 - len(pithy_summary) / len(full_summary)) * 100
    print(f"   Reduction: {reduction_pct:.1f}%\n")

if __name__ == "__main__":
    main()
