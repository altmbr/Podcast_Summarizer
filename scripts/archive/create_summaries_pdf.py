#!/usr/bin/env python3
"""
Create a PDF from all podcast summaries, ordered by date (most recent first)
"""

import os
import re
from pathlib import Path
from datetime import datetime
import subprocess

def extract_date_from_summary(summary_path):
    """Extract the date from a summary.md file"""
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for **Date:** line
    date_match = re.search(r'\*\*Date:\*\*\s*(.+)', content)
    if date_match:
        date_str = date_match.group(1).strip()

        # Try to parse different date formats
        # Format: "November 03, 2025" or "2025-11-03" or "20251103"
        for fmt in ['%B %d, %Y', '%Y-%m-%d', '%Y%m%d']:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue

        # If we can't parse, return a very old date so it goes to the end
        return datetime(1900, 1, 1)

    return datetime(1900, 1, 1)

def main():
    podcast_work_dir = Path("./podcast_work")

    # Find all summary.md files
    summary_files = list(podcast_work_dir.rglob("summary.md"))

    print(f"Found {len(summary_files)} summary files")

    # Extract dates and sort
    summaries_with_dates = []
    for summary_path in summary_files:
        date = extract_date_from_summary(summary_path)
        summaries_with_dates.append((date, summary_path))

    # Sort by date (most recent first)
    summaries_with_dates.sort(key=lambda x: x[0], reverse=True)

    # Create combined markdown file
    combined_md_path = Path("./all_summaries.md")

    print(f"Creating combined markdown file: {combined_md_path}")

    with open(combined_md_path, 'w', encoding='utf-8') as outfile:
        # Write title page
        outfile.write("# Podcast Summaries\n\n")
        outfile.write(f"**Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n\n")
        outfile.write(f"**Total Episodes:** {len(summaries_with_dates)}\n\n")
        outfile.write("---\n\n")

        # Write each summary
        for idx, (date, summary_path) in enumerate(summaries_with_dates, 1):
            print(f"  [{idx}/{len(summaries_with_dates)}] Adding: {summary_path.parent.name}")

            # Read the summary
            with open(summary_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

            # Add the summary with a separator
            outfile.write(content)
            outfile.write("\n\n")
            outfile.write("=" * 80)
            outfile.write("\n\n")
            outfile.write("\\pagebreak\n\n")  # Force page break in PDF

    print(f"✓ Combined markdown created: {combined_md_path}")

    # Convert to PDF using pandoc
    pdf_path = Path("./all_summaries.pdf")

    print(f"\nConverting to PDF: {pdf_path}")

    try:
        # Try pandoc first
        cmd = [
            "pandoc",
            str(combined_md_path),
            "-o", str(pdf_path),
            "--pdf-engine=xelatex",  # Better Unicode support
            "-V", "geometry:margin=1in",
            "-V", "fontsize=11pt",
            "--toc",  # Table of contents
            "--toc-depth=2"
        ]

        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ PDF created successfully: {pdf_path}")
        print(f"\n📄 {len(summaries_with_dates)} summaries compiled into PDF")

    except FileNotFoundError:
        print("❌ Error: pandoc not found")
        print("   Install with: brew install pandoc")
        print(f"   Markdown file saved to: {combined_md_path}")
        print("   You can manually convert it to PDF")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error converting to PDF: {e}")
        print(f"   Markdown file saved to: {combined_md_path}")
        if e.stderr:
            print(f"   Error details: {e.stderr}")

if __name__ == "__main__":
    main()
