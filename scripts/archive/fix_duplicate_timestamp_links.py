#!/usr/bin/env python3
"""
Fix duplicate/nested timestamp links in summary.md files.

Converts patterns like:
[[[[00:22:00]](url)](url)](url)

To:
[[00:22:00]](url)
"""

import os
import re
from pathlib import Path

def fix_nested_links(content):
    """
    Fix nested timestamp links in markdown content.

    Pattern to match:
    [[[[timestamp]](url)](url)](url) or similar nested patterns
    """
    # Pattern to match the nested structure: [[[[timestamp]](url)](url)](url)
    # This matches 4 opening brackets, timestamp, then repeated (url) patterns
    pattern = r'\[\[\[\[(\d{1,2}:\d{2}:\d{2})\]\]\(([^)]+)\)\]\([^)]+\)\]\([^)]+\)'

    def replace_nested(match):
        timestamp = match.group(1)
        url = match.group(2)
        # Return clean format: [[timestamp]](url)
        return f'[[{timestamp}]]({url})'

    # Apply the replacement
    content = re.sub(pattern, replace_nested, content)

    # Also handle triple nested: [[[timestamp]](url)](url)
    pattern_triple = r'\[\[\[(\d{1,2}:\d{2}:\d{2})\]\]\(([^)]+)\)\]\([^)]+\)'
    content = re.sub(pattern_triple, lambda m: f'[[{m.group(1)}]]({m.group(2)})', content)

    # Also handle double nested: [[timestamp]](url)](url)
    pattern_double = r'\[\[(\d{1,2}:\d{2}:\d{2})\]\]\(([^)]+)\)\]\([^)]+\)'
    content = re.sub(pattern_double, lambda m: f'[[{m.group(1)}]]({m.group(2)})', content)

    return content

def process_summary_file(file_path):
    """Process a single summary.md file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        fixed_content = fix_nested_links(original_content)

        if fixed_content != original_content:
            # Count how many fixes were made
            original_count = original_content.count('[[[[')
            fixed_count = fixed_content.count('[[[[')
            fixes_made = original_count - fixed_count

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)

            return True, fixes_made

        return False, 0

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, 0

def main():
    podcast_work_dir = Path(__file__).parent / 'podcast_work'

    if not podcast_work_dir.exists():
        print(f"Error: {podcast_work_dir} does not exist")
        return

    print("Scanning for summary.md files with nested timestamp links...\n")

    files_fixed = 0
    total_fixes = 0

    # Find all summary.md files
    for summary_file in podcast_work_dir.rglob('summary.md'):
        fixed, fixes = process_summary_file(summary_file)

        if fixed:
            files_fixed += 1
            total_fixes += fixes
            podcast_name = summary_file.parent.parent.name
            episode_name = summary_file.parent.name
            print(f"✓ Fixed {podcast_name}/{episode_name}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files processed: {files_fixed}")
    print(f"  Nested links fixed: ~{total_fixes} locations")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
