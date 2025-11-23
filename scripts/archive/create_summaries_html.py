#!/usr/bin/env python3
"""
Create an HTML file from all podcast summaries, ordered by date (most recent first)
This can be easily printed to PDF from any browser
"""

import os
import re
from pathlib import Path
from datetime import datetime
import markdown

def extract_date_from_summary(summary_path):
    """Extract the date from a summary.md file"""
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for **Date:** line
    date_match = re.search(r'\*\*Date:\*\*\s*(.+)', content)
    if date_match:
        date_str = date_match.group(1).strip()

        # Try to parse different date formats
        for fmt in ['%B %d, %Y', '%Y-%m-%d', '%Y%m%d']:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue

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

    # Create combined markdown first
    combined_md = []
    combined_md.append("# Podcast Summaries\n\n")
    combined_md.append(f"**Generated:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}\n\n")
    combined_md.append(f"**Total Episodes:** {len(summaries_with_dates)}\n\n")
    combined_md.append("---\n\n")

    for idx, (date, summary_path) in enumerate(summaries_with_dates, 1):
        print(f"  [{idx}/{len(summaries_with_dates)}] Adding: {summary_path.parent.name}")

        with open(summary_path, 'r', encoding='utf-8') as infile:
            content = infile.read()

        combined_md.append(content)
        combined_md.append("\n\n---\n\n")
        if idx < len(summaries_with_dates):  # Don't add page break after last one
            combined_md.append('<div style="page-break-after: always;"></div>\n\n')

    markdown_content = ''.join(combined_md)

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=['extra', 'nl2br'])

    # Create full HTML document with styling
    html_doc = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Podcast Summaries</title>
    <style>
        @media print {{
            body {{
                font-family: Georgia, serif;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 3px solid #3498db;
                padding-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
                border-bottom: 2px solid #95a5a6;
                padding-bottom: 5px;
            }}
            h3 {{
                color: #7f8c8d;
                margin-top: 20px;
            }}
            strong {{
                color: #2980b9;
            }}
            blockquote {{
                border-left: 4px solid #3498db;
                padding-left: 15px;
                margin-left: 0;
                font-style: italic;
                color: #555;
            }}
            hr {{
                border: none;
                border-top: 2px solid #ecf0f1;
                margin: 40px 0;
            }}
        }}

        body {{
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 5px;
        }}
        h3 {{
            color: #7f8c8d;
            margin-top: 20px;
        }}
        strong {{
            color: #2980b9;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-left: 0;
            font-style: italic;
            color: #555;
            background-color: #f8f9fa;
            padding: 10px 15px;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 40px 0;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "Courier New", monospace;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""

    # Save HTML file
    html_path = Path("./all_summaries.html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)

    print(f"\n✓ HTML file created: {html_path}")
    print(f"\n📄 {len(summaries_with_dates)} summaries compiled")
    print(f"\n💡 To create PDF:")
    print(f"   1. Open {html_path} in your browser")
    print(f"   2. Press Cmd+P (Print)")
    print(f"   3. Select 'Save as PDF' as the destination")
    print(f"   4. Click 'Save'")

if __name__ == "__main__":
    main()
