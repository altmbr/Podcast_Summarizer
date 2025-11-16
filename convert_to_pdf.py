#!/usr/bin/env python3
"""
Convert markdown to PDF using markdown + fpdf2
"""

import sys
from pathlib import Path

try:
    import markdown
    from fpdf import FPDF
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "fpdf2"])
    import markdown
    from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, '', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def markdown_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF"""
    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to plain text (simplified)
    # For better results, we'd parse the HTML, but for now we'll just clean up the markdown
    lines = md_content.split('\n')

    # Create PDF
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    for line in lines:
        # Determine formatting based on markdown syntax
        if line.startswith('# '):
            pdf.set_font('Arial', 'B', 16)
            pdf.multi_cell(0, 10, line[2:])
            pdf.ln(2)
        elif line.startswith('## '):
            pdf.set_font('Arial', 'B', 14)
            pdf.multi_cell(0, 8, line[3:])
            pdf.ln(1)
        elif line.startswith('### '):
            pdf.set_font('Arial', 'B', 12)
            pdf.multi_cell(0, 7, line[4:])
            pdf.ln(1)
        elif line.startswith('- ') or line.startswith('* '):
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(0, 5, '  • ' + line[2:])
        elif line.startswith('**') and line.endswith('**'):
            pdf.set_font('Arial', 'B', 10)
            pdf.multi_cell(0, 5, line.strip('*'))
        elif line.strip() == '':
            pdf.ln(2)
        else:
            pdf.set_font('Arial', '', 10)
            # Handle bold text
            if '**' in line:
                # Simple handling - not perfect but works
                line = line.replace('**', '')
            pdf.multi_cell(0, 5, line)

    # Save PDF
    pdf.output(pdf_file)
    print(f"✓ PDF created: {pdf_file}")

if __name__ == "__main__":
    md_file = Path("weekly_summaries/weekly_summary_2025-11-04_to_2025-11-11.md")
    pdf_file = Path("weekly_summaries/weekly_summary_2025-11-04_to_2025-11-11.pdf")

    markdown_to_pdf(md_file, pdf_file)
