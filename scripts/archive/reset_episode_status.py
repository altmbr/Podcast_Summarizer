#!/usr/bin/env python3
"""Reset status of specific episodes to 'transcribed' so they can be re-summarized."""

import json

# Load the status file
with open('podcast_status.json', 'r', encoding='utf-8') as f:
    status = json.load(f)

# Episode identifiers to reset (video IDs or episode titles)
episodes_to_reset = [
    "AI Robots for Your Laundry",
    "Pylon:",
    "Xpeng's Newly Appointed",
    "Satya Nadella describes",
    "Marc Andreessen, Ben Horowitz"
]

count = 0
# Iterate through all podcasts and episodes
for podcast_url, podcast_data in status.get('podcasts', {}).items():
    for episode_id, episode_data in podcast_data.get('episodes', {}).items():
        title = episode_data.get('title', '')
        # Check if this episode matches any of our reset targets
        for reset_target in episodes_to_reset:
            if reset_target in title:
                if episode_data.get('status') == 'summarized':
                    episode_data['status'] = 'transcribed'
                    print(f"Reset: {title}")
                    count += 1
                    break

# Save the updated status
with open('podcast_status.json', 'w', encoding='utf-8') as f:
    json.dump(status, f, indent=2, ensure_ascii=False)

print(f"\nReset {count} episodes to 'transcribed' status")
