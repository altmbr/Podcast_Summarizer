#!/usr/bin/env python3
"""
Convert markdown to well-formatted PDF with working links
"""

import sys
import subprocess
from pathlib import Path

def markdown_to_pdf(md_file, pdf_file):
    """Convert markdown to PDF via HTML with proper formatting and links"""

    md_path = Path(md_file)
    pdf_path = Path(pdf_file)
    html_path = md_path.with_suffix('.html')

    # Custom CSS for better formatting
    css = """
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 20px;
            color: #333;
            font-size: 11pt;
        }
        h1 {
            color: #1a1a1a;
            border-bottom: 2px solid #e1e4e8;
            padding-bottom: 0.3em;
            font-size: 24pt;
            margin-top: 24px;
            margin-bottom: 16px;
        }
        h2 {
            color: #1a1a1a;
            border-bottom: 1px solid #e1e4e8;
            padding-bottom: 0.3em;
            font-size: 18pt;
            margin-top: 20px;
            margin-bottom: 12px;
        }
        h3 {
            color: #1a1a1a;
            font-size: 14pt;
            margin-top: 16px;
            margin-bottom: 8px;
        }
        p {
            margin-bottom: 12px;
        }
        ul, ol {
            margin-bottom: 12px;
            padding-left: 2em;
        }
        li {
            margin-bottom: 6px;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        blockquote {
            margin: 0;
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
        }
        code {
            background-color: #f6f8fa;
            border-radius: 3px;
            padding: 0.2em 0.4em;
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
        }
        strong {
            font-weight: 600;
        }
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #e1e4e8;
            border: 0;
        }
        @page {
            margin: 0.75in;
        }
    </style>
    """

    # Convert markdown to HTML with pandoc
    print(f"Converting {md_path.name} to HTML...")
    subprocess.run([
        'pandoc',
        str(md_path),
        '-o', str(html_path),
        '--standalone',
        '--metadata', f'title={md_path.stem}',
        '-H', '/dev/stdin'
    ], input=css.encode(), check=True)

    # Convert HTML to PDF with Chrome headless
    print(f"Converting HTML to PDF...")
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    subprocess.run([
        chrome_path,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--print-to-pdf=' + str(pdf_path),
        f'file://{html_path.absolute()}'
    ], check=True, capture_output=True)

    # Clean up HTML file
    html_path.unlink()

    # Get file size
    size_kb = pdf_path.stat().st_size / 1024
    print(f"✓ PDF created: {pdf_path.name} ({size_kb:.0f} KB)")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_md_to_pdf.py <markdown_file> [output_pdf]")
        sys.exit(1)

    md_file = sys.argv[1]

    if len(sys.argv) >= 3:
        pdf_file = sys.argv[2]
    else:
        pdf_file = Path(md_file).with_suffix('.pdf')

    markdown_to_pdf(md_file, pdf_file)

if __name__ == "__main__":
    main()
