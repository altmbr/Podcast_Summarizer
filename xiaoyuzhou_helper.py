#!/usr/bin/env python3
"""
Helper functions for downloading podcasts from Xiaoyuzhou (小宇宙)
"""

import requests
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

def extract_podcast_id_from_url(url):
    """Extract podcast ID from Xiaoyuzhou URL

    Examples:
        https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962 -> 626b46ea9cbbf0451cf5a962
        https://www.xiaoyuzhoufm.com/episode/68ae86d18ce45d46d49c4d50 -> 68ae86d18ce45d46d49c4d50
    """
    match = re.search(r'/(?:podcast|episode)/([a-f0-9]+)', url)
    if match:
        return match.group(1)
    return None

def is_xiaoyuzhou_url(url):
    """Check if URL is a Xiaoyuzhou podcast or episode URL"""
    return 'xiaoyuzhoufm.com' in url

def get_xiaoyuzhou_podcast_episodes(podcast_url, first_run=False):
    """
    Get episode list from a Xiaoyuzhou podcast URL

    Args:
        podcast_url: Full URL to Xiaoyuzhou podcast (e.g., https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962)
        first_run: If True, only return the latest episode

    Returns:
        List of episode dicts with keys: id, url, title, upload_date (YYYYMMDD format)
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(podcast_url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching podcast page: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Try to find JSON data in script tags
    episodes = []

    # Look for Next.js data in script tags
    scripts = soup.find_all('script', type='application/json')
    for script in scripts:
        try:
            data = json.loads(script.string)
            # Navigate the Next.js data structure to find episodes
            # This structure may vary, but typically found in __NEXT_DATA__
            if isinstance(data, dict):
                episodes_data = _extract_episodes_from_json(data)
                if episodes_data:
                    episodes = episodes_data
                    break
        except (json.JSONDecodeError, KeyError, TypeError):
            continue

    # Fallback: Try to find __NEXT_DATA__ in inline scripts
    if not episodes:
        for script in soup.find_all('script', id='__NEXT_DATA__'):
            try:
                data = json.loads(script.string)
                episodes_data = _extract_episodes_from_json(data)
                if episodes_data:
                    episodes = episodes_data
                    break
            except (json.JSONDecodeError, KeyError, TypeError):
                continue

    # Sort by publication date (newest first)
    episodes.sort(key=lambda x: x.get('upload_date', '0'), reverse=True)

    # On first run, only return the latest episode
    if first_run and episodes:
        episodes = [episodes[0]]

    return episodes

def _extract_episodes_from_json(data):
    """
    Recursively search for episodes array in JSON data
    Returns list of episode dicts
    """
    episodes = []

    if isinstance(data, dict):
        # Check if this dict contains episode data
        if 'episodes' in data and isinstance(data['episodes'], list):
            for ep in data['episodes']:
                if isinstance(ep, dict) and 'eid' in ep:
                    episode_id = ep.get('eid')
                    title = ep.get('title', 'Unknown')

                    # Extract publication date
                    pub_date = ep.get('pubDate') or ep.get('pubdate')
                    if pub_date:
                        # Convert ISO date or timestamp to YYYYMMDD
                        upload_date = _parse_date_to_yyyymmdd(pub_date)
                    else:
                        upload_date = '0'

                    episode_url = f"https://www.xiaoyuzhoufm.com/episode/{episode_id}"

                    episodes.append({
                        'id': episode_id,
                        'url': episode_url,
                        'title': title,
                        'upload_date': upload_date
                    })
            return episodes

        # Recursively search nested dicts
        for key, value in data.items():
            result = _extract_episodes_from_json(value)
            if result:
                episodes.extend(result)

    elif isinstance(data, list):
        for item in data:
            result = _extract_episodes_from_json(item)
            if result:
                episodes.extend(result)

    return episodes

def _parse_date_to_yyyymmdd(date_value):
    """
    Convert various date formats to YYYYMMDD string

    Handles:
        - ISO timestamps (2024-11-06T12:00:00Z)
        - Unix timestamps (milliseconds or seconds)
        - YYYY-MM-DD strings
    """
    if isinstance(date_value, str):
        # Try ISO format
        try:
            dt = datetime.fromisoformat(date_value.replace('Z', '+00:00'))
            return dt.strftime('%Y%m%d')
        except:
            pass

        # Try YYYY-MM-DD
        try:
            dt = datetime.strptime(date_value[:10], '%Y-%m-%d')
            return dt.strftime('%Y%m%d')
        except:
            pass

    elif isinstance(date_value, (int, float)):
        # Unix timestamp (assume milliseconds if > 1e10)
        try:
            if date_value > 1e10:
                date_value = date_value / 1000
            dt = datetime.fromtimestamp(date_value)
            return dt.strftime('%Y%m%d')
        except:
            pass

    return '0'

def extract_audio_url_from_episode_page(episode_url):
    """
    Extract the direct audio file URL from a Xiaoyuzhou episode page

    Args:
        episode_url: Full URL to episode (e.g., https://www.xiaoyuzhoufm.com/episode/68ae86d18ce45d46d49c4d50)

    Returns:
        Tuple of (audio_url, episode_title) or (None, None) if not found
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(episode_url, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching episode page: {e}")
        return None, None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Method 1: Try og:audio meta tag (most reliable)
    meta_tag = soup.find('meta', property='og:audio')
    if meta_tag and meta_tag.get('content'):
        audio_url = meta_tag['content']

        # Get title from og:title
        title_tag = soup.find('meta', property='og:title')
        title = title_tag['content'] if title_tag else 'Unknown'

        return audio_url, title

    # Method 2: Try to find <audio> tag
    audio_tag = soup.find('audio')
    if audio_tag and audio_tag.get('src'):
        audio_url = audio_tag['src']

        # Try to get title from page
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else 'Unknown'

        return audio_url, title

    # Method 3: Search for media.xyzcdn.net URLs in the HTML
    html_content = str(soup)
    audio_pattern = r'https://media\.xyzcdn\.net/[^"\']+\.(?:mp3|m4a|mp4a)'
    matches = re.findall(audio_pattern, html_content)
    if matches:
        audio_url = matches[0]  # Take the first match

        # Try to get title
        title_tag = soup.find('meta', property='og:title') or soup.find('h1')
        title = title_tag.get('content' if title_tag.name == 'meta' else 'text', 'Unknown')

        return audio_url, title

    return None, None

def download_xiaoyuzhou_audio(episode_url, output_path):
    """
    Download audio from a Xiaoyuzhou episode URL

    Args:
        episode_url: URL to the episode page
        output_path: Path where the audio file should be saved

    Returns:
        True if successful, False otherwise
    """
    print(f"  → Extracting audio URL from episode page...")
    audio_url, title = extract_audio_url_from_episode_page(episode_url)

    if not audio_url:
        print(f"  ❌ Could not find audio URL on episode page")
        return False

    print(f"  → Found audio URL: {audio_url[:60]}...")
    print(f"  → Downloading audio to: {output_path}")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }

        response = requests.get(audio_url, headers=headers, stream=True, timeout=60)
        response.raise_for_status()

        # Get total file size for progress tracking
        total_size = int(response.headers.get('content-length', 0))

        with open(output_path, 'wb') as f:
            if total_size == 0:
                f.write(response.content)
            else:
                downloaded = 0
                chunk_size = 1024 * 1024  # 1MB chunks
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        percent = (downloaded / total_size) * 100
                        print(f"\r  → Progress: {percent:.1f}%", end='', flush=True)
                print()  # New line after progress

        print(f"  ✓ Audio downloaded successfully")
        return True

    except Exception as e:
        print(f"  ❌ Error downloading audio: {e}")
        return False

def extract_xiaoyuzhou_podcast_name(podcast_url):
    """
    Extract podcast name from Xiaoyuzhou podcast URL by fetching the page

    Returns:
        Podcast name or None if not found
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    try:
        response = requests.get(podcast_url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Try og:title meta tag
        title_tag = soup.find('meta', property='og:title')
        if title_tag and title_tag.get('content'):
            return title_tag['content']

        # Fallback to h1
        h1_tag = soup.find('h1')
        if h1_tag:
            return h1_tag.get_text(strip=True)

    except Exception as e:
        print(f"Warning: Could not extract podcast name: {e}")

    return None
