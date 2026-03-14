#!/usr/bin/env python3
"""
Look up Podscan podcast IDs for all podcasts in podcast_config.json.
Searches the Podscan API by podcast name and prints matches for manual review.

Usage:
    PODSCAN_API_KEY=xxx python cloud/scripts/lookup_podscan_ids.py
"""

import json
import os
import sys
import time

import requests

PODSCAN_API_KEY = os.environ.get("PODSCAN_API_KEY")
if not PODSCAN_API_KEY:
    print("Error: PODSCAN_API_KEY environment variable required")
    sys.exit(1)

BASE_URL = "https://podscan.fm/api/v1"
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "podcast_config.json")


def search_podcast(name: str, max_retries: int = 5) -> list[dict]:
    """Search Podscan for a podcast by name."""
    for attempt in range(max_retries):
        resp = requests.get(
            f"{BASE_URL}/podcasts",
            headers={"Authorization": f"Bearer {PODSCAN_API_KEY}"},
            params={"query": name, "limit": 5},
            timeout=30,
        )
        if resp.status_code == 429:
            time.sleep(5 * (attempt + 1))
            continue
        resp.raise_for_status()
        data = resp.json()
        return data.get("podcasts", data.get("data", []))

    raise RuntimeError(f"Rate limited after {max_retries} retries searching for: {name}")


def main():
    with open(CONFIG_PATH) as f:
        config = json.load(f)

    updates = {}

    for podcast_name, info in config.items():
        existing_id = info.get("podscan_id", "")
        if existing_id:
            print(f"[SKIP] {podcast_name} — already has podscan_id: {existing_id}")
            continue

        # Skip Chinese podcasts (Xiaoyuzhou platform, not on Podscan)
        if any(ord(c) > 127 for c in podcast_name[:3]):
            print(f"[SKIP] {podcast_name} — Chinese podcast (not on Podscan)")
            continue

        print(f"\n[SEARCH] {podcast_name}...")
        try:
            results = search_podcast(podcast_name)
        except Exception as e:
            print(f"  Error: {e}")
            continue

        if not results:
            print(f"  No results found")
            continue

        for i, r in enumerate(results):
            pid = r.get("id", "")
            title = r.get("title", r.get("name", ""))
            print(f"  [{i+1}] {pid} — {title}")

        # Auto-select if only one result or first result matches closely
        if len(results) == 1:
            selected = results[0]
            pid = selected.get("id", "")
            print(f"  → Auto-selected: {pid}")
            updates[podcast_name] = pid
        else:
            choice = input(f"  Select (1-{len(results)}, or ENTER to skip): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(results):
                selected = results[int(choice) - 1]
                pid = selected.get("id", "")
                updates[podcast_name] = pid
                print(f"  → Selected: {pid}")

        time.sleep(1)  # Rate limit courtesy

    if updates:
        print(f"\n{'='*60}")
        print(f"Updating {len(updates)} podcast(s) in podcast_config.json...")

        for name, pid in updates.items():
            config[name]["podscan_id"] = pid

        with open(CONFIG_PATH, "w") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
            f.write("\n")

        print("Done! Updated podcast_config.json")
        print("\nUpdated podcasts:")
        for name, pid in updates.items():
            print(f"  {name}: {pid}")
    else:
        print("\nNo updates to make.")


if __name__ == "__main__":
    main()
