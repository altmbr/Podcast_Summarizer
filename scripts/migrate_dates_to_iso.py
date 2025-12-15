#!/usr/bin/env python3
"""
Migrate all summary.md and transcript.md files to use ISO date format (YYYY-MM-DD)
Converts: "December 12, 2025" → "2025-12-12"
"""

import re
from pathlib import Path
from datetime import datetime

# Month name to number mapping
MONTH_MAP = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4,
    'may': 5, 'june': 6, 'july': 7, 'august': 8,
    'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def convert_date_to_iso(date_str: str) -> str:
    """
    Convert date from human-readable to ISO format
    Input: "December 12, 2025" or "December 12 2025"
    Output: "2025-12-12"
    """
    # Try to parse human-readable format
    match = re.match(r'^([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})$', date_str.strip())
    if match:
        month_name, day, year = match.groups()
        month_num = MONTH_MAP.get(month_name.lower())
        if month_num:
            return f"{year}-{month_num:02d}-{int(day):02d}"

    # Already in ISO format or other format - return as is
    return date_str

def migrate_file(file_path: Path) -> bool:
    """
    Migrate a single markdown file
    Returns True if file was modified
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # Find and replace **Date:** lines
        def replace_date(match):
            original_date = match.group(1)
            iso_date = convert_date_to_iso(original_date)
            if iso_date != original_date:
                print(f"  {file_path.name}: {original_date} → {iso_date}")
                return f"**Date:** {iso_date}"
            return match.group(0)

        # Replace date in metadata section
        content = re.sub(
            r'\*\*Date:\*\*\s+(.+)',
            replace_date,
            content
        )

        # Write back if changed
        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True

        return False
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main migration script"""
    podcast_work_dir = Path("podcast_work")

    if not podcast_work_dir.exists():
        print("❌ Error: podcast_work directory not found")
        return

    print("🔄 Migrating dates to ISO format (YYYY-MM-DD)")
    print("=" * 60)

    # Find all summary.md and transcript.md files
    summary_files = list(podcast_work_dir.glob("*/*/summary.md"))
    transcript_files = list(podcast_work_dir.glob("*/*/transcript.md"))

    all_files = summary_files + transcript_files

    print(f"\nFound {len(all_files)} files to process:")
    print(f"  - {len(summary_files)} summary.md files")
    print(f"  - {len(transcript_files)} transcript.md files")
    print()

    modified_count = 0
    unchanged_count = 0

    for file_path in all_files:
        podcast_name = file_path.parent.parent.name
        episode_name = file_path.parent.name

        # Only print if we're about to modify
        was_modified = migrate_file(file_path)

        if was_modified:
            modified_count += 1
        else:
            unchanged_count += 1

    print()
    print("=" * 60)
    print("✅ Migration complete!")
    print(f"  - Modified: {modified_count} files")
    print(f"  - Unchanged: {unchanged_count} files")
    print(f"  - Total: {len(all_files)} files")

if __name__ == "__main__":
    main()
