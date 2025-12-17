#!/usr/bin/env python3
"""
Main entry point for Cloud Run job.
Processes selected podcast episodes: download → transcribe → diarize → identify speakers → summarize → push to git.
"""

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
import re

from .config import Config
from .download import download_audio
from .transcribe import transcribe_audio
from .diarize import diarize_audio
from .merge_transcript import merge_transcript_with_diarization
from .speaker_id import identify_speakers
from .summarize import summarize_transcript
from .git_ops import GitRepo
from .status import update_podcast_status


def process_episode(episode: dict, config: Config, repo: GitRepo, work_dir: Path) -> bool:
    """Process a single episode through the full pipeline."""

    video_id = episode["video_id"]
    title = episode["title"]
    podcast_name = episode["podcast_name"]
    video_url = episode.get("video_url", f"https://youtube.com/watch?v={video_id}")
    podcast_url = episode.get("podcast_url", "")
    upload_date = episode.get("upload_date", "")

    print(f"\n{'='*80}")
    print(f"Processing: {title}")
    print(f"Podcast: {podcast_name}")
    print(f"Video ID: {video_id}")
    print(f"{'='*80}\n")

    # Sanitize title for folder name
    sanitized_title = re.sub(r'[<>:"/\\|?*]', '_', title)
    sanitized_title = sanitized_title[:200]  # Limit length

    episode_dir = repo.path / "podcast_work" / podcast_name / sanitized_title
    episode_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Step 1: Download audio
        print("Step 1/6: Downloading audio...")
        audio_path = work_dir / f"{video_id}.mp3"
        download_audio(video_url, audio_path)

        # Copy to episode dir
        import shutil
        shutil.copy(audio_path, episode_dir / "raw_podcast.mp3")

        # Step 2: Transcribe
        print("\nStep 2/6: Transcribing with Faster-Whisper...")
        segments = transcribe_audio(audio_path, model_size="large-v3")

        # Save transcript immediately after transcription (before diarization)
        # This ensures we have the transcript even if diarization fails
        # Using a separate file so we don't overwrite transcript_raw.md
        transcript_whisper_path = episode_dir / "transcript_whisper.md"
        transcript_lines = []
        for seg in segments:
            start_min = int(seg["start"] // 60)
            start_sec = int(seg["start"] % 60)
            timestamp = f"[{start_min:02d}:{start_sec:02d}]"
            transcript_lines.append(f"{timestamp} {seg['text'].strip()}")
        initial_transcript = "\n\n".join(transcript_lines)
        with open(transcript_whisper_path, "w") as f:
            f.write(f"# Transcript (Whisper only - no speaker labels)\n\n{initial_transcript}")
        print(f"  ✓ Saved Whisper transcript: {transcript_whisper_path}")

        # Step 3: Diarize
        print("\nStep 3/6: Diarizing with Pyannote...")
        diarization = diarize_audio(audio_path, config.huggingface_token)

        # Step 4: Merge transcription with diarization
        print("\nStep 4/6: Merging transcript with speaker labels...")
        transcript_raw = merge_transcript_with_diarization(segments, diarization)

        # Save transcript_raw.md (with SPEAKER_XX labels)
        transcript_raw_path = episode_dir / "transcript_raw.md"
        with open(transcript_raw_path, "w") as f:
            f.write(transcript_raw)
        print(f"  ✓ Saved transcript with speaker labels: {transcript_raw_path}")

        # Step 5: Identify speakers (Claude Haiku)
        print("\nStep 5/6: Identifying speakers with Claude Haiku...")
        transcript = identify_speakers(
            transcript_raw,
            title,
            config.anthropic_api_key
        )

        # Save transcript.md
        transcript_path = episode_dir / "transcript.md"
        with open(transcript_path, "w") as f:
            f.write(transcript)

        # Step 6: Summarize (Claude Sonnet)
        print("\nStep 6/6: Summarizing with Claude Sonnet...")
        summary = summarize_transcript(
            transcript,
            title,
            podcast_name,
            video_url,
            upload_date,
            config.anthropic_api_key
        )

        # Save summary.md
        summary_path = episode_dir / "summary.md"
        with open(summary_path, "w") as f:
            f.write(summary)

        # Update podcast_status.json
        if podcast_url:
            update_podcast_status(
                repo.path / "podcast_status.json",
                podcast_url,
                video_id,
                "summarized"
            )

        print(f"\n{'='*80}")
        print(f"✓ Successfully processed: {title}")
        print(f"{'='*80}\n")
        return True

    except Exception as e:
        print(f"\n{'='*80}")
        print(f"✗ Error processing {title}: {e}")
        print(f"{'='*80}\n")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(description="Process podcast episodes")
    parser.add_argument("--episodes", help="JSON string of episodes to process (or use EPISODES env var)")
    parser.add_argument("--dry-run", action="store_true", help="Don't push to git")
    args = parser.parse_args()

    # Load configuration
    try:
        config = Config.from_environment()
    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

    # Parse episodes from --episodes arg or EPISODES env var
    episodes_json = args.episodes or os.environ.get("EPISODES")
    if not episodes_json:
        print("Error: Must provide --episodes argument or EPISODES environment variable")
        sys.exit(1)

    try:
        episodes = json.loads(episodes_json)
    except json.JSONDecodeError as e:
        print(f"Invalid episodes JSON: {e}")
        sys.exit(1)

    print(f"Processing {len(episodes)} episode(s)")

    # Create temporary working directory
    with tempfile.TemporaryDirectory() as work_dir:
        work_path = Path(work_dir)

        # Clone repository
        print("Cloning repository...")
        repo_url = f"https://{config.github_token}@github.com/altmbr/Podcast_Summarizer.git"
        repo = GitRepo.clone(repo_url, work_path / "repo")

        # Process each episode
        results = []
        for episode in episodes:
            success = process_episode(episode, config, repo, work_path)
            results.append({"episode": episode["title"], "success": success})

        # Commit and push
        if not args.dry_run:
            successful = [r for r in results if r["success"]]
            if successful:
                commit_msg = f"Add {len(successful)} new podcast episode(s)\n\n"
                commit_msg += "\n".join([f"- {r['episode']}" for r in successful])
                commit_msg += "\n\n🤖 Generated with Cloud Pipeline"

                repo.add_all()
                repo.commit(commit_msg)
                repo.push()
                print(f"\n✓ Pushed {len(successful)} episode(s) to GitHub")
        else:
            print("\n[DRY RUN] Skipping git push")

        # Print summary
        print(f"\n{'='*80}")
        print("PROCESSING SUMMARY")
        print(f"{'='*80}")
        for r in results:
            status = "✓" if r["success"] else "✗"
            print(f"  {status} {r['episode']}")
        print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
