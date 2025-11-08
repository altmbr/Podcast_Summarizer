#!/usr/bin/env python3
"""
Summary Tester: Generate and compare summaries using different prompts.
Allows iterating on summarization prompts and comparing results side-by-side.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Setup paths
TRANSCRIPTS_DIR = Path("podcast_work")
SUMMARIES_DIR = Path("summary_tests")
PROMPTS_DIR = Path("summary_prompts")

# Create directories if they don't exist
SUMMARIES_DIR.mkdir(exist_ok=True)
PROMPTS_DIR.mkdir(exist_ok=True)

def find_transcripts():
    """Find all transcript.md files in the podcast_work directory."""
    transcripts = list(TRANSCRIPTS_DIR.rglob("transcript.md"))
    return sorted(transcripts)

def load_prompt(prompt_name):
    """Load a prompt file from the summary_prompts directory."""
    prompt_path = PROMPTS_DIR / f"{prompt_name}.md"
    if not prompt_path.exists():
        print(f"Error: Prompt file not found: {prompt_path}")
        return None

    with open(prompt_path, 'r') as f:
        return f.read()

def list_available_prompts():
    """List all available prompt files."""
    prompts = sorted([p.stem for p in PROMPTS_DIR.glob("*.md")])
    return prompts

def generate_summary(transcript_path, prompt_text, transcript_excerpt_length=4000):
    """Generate a summary using the OpenAI API."""

    # Read transcript
    with open(transcript_path, 'r') as f:
        transcript_text = f.read()

    # Extract episode title from path or filename
    # Try to get from parent directory names
    parts = transcript_path.parent.parts
    episode_title = parts[-1] if len(parts) > 0 else "Unknown Episode"
    podcast_name = parts[-2] if len(parts) > 1 else "Unknown Podcast"

    # Prepare the prompt
    summary_prompt = f"""{prompt_text}

Podcast: {podcast_name}
Episode: {episode_title}

Transcript excerpt (first {transcript_excerpt_length} characters):
{transcript_text[:transcript_excerpt_length]}...

Please provide a comprehensive summary."""

    print(f"Generating summary for: {podcast_name} - {episode_title}")
    print(f"Prompt length: {len(prompt_text)} characters")
    print(f"Transcript excerpt: {len(transcript_text[:transcript_excerpt_length])} characters")

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert podcast summarizer. Follow the instructions in the user prompt carefully."
                },
                {
                    "role": "user",
                    "content": summary_prompt
                }
            ],
            temperature=0.7,
            max_tokens=2000
        )

        summary_text = response.choices[0].message.content
        return summary_text

    except Exception as e:
        print(f"Error generating summary: {e}")
        return None

def save_summary_result(transcript_path, prompt_name, summary_text):
    """Save the summary result with metadata."""

    # Create a test result directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_id = f"{prompt_name}_{timestamp}"

    result_dir = SUMMARIES_DIR / test_id
    result_dir.mkdir(exist_ok=True)

    # Save the summary
    summary_file = result_dir / "summary.md"
    with open(summary_file, 'w') as f:
        f.write(summary_text)

    # Save metadata
    metadata = {
        "test_id": test_id,
        "timestamp": timestamp,
        "prompt_name": prompt_name,
        "transcript_path": str(transcript_path),
        "summary_file": str(summary_file),
        "prompt_file": str(PROMPTS_DIR / f"{prompt_name}.md")
    }

    metadata_file = result_dir / "metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    return test_id, result_dir

def list_test_results():
    """List all saved test results."""
    if not SUMMARIES_DIR.exists():
        print("No test results yet.")
        return []

    results = sorted([d.name for d in SUMMARIES_DIR.iterdir() if d.is_dir()])
    return results

def show_test_result(test_id):
    """Display a saved test result."""
    result_dir = SUMMARIES_DIR / test_id

    if not result_dir.exists():
        print(f"Test result not found: {test_id}")
        return

    # Load metadata
    metadata_file = result_dir / "metadata.json"
    if metadata_file.exists():
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)

        print(f"\n{'='*70}")
        print(f"Test ID: {metadata['test_id']}")
        print(f"Timestamp: {metadata['timestamp']}")
        print(f"Prompt: {metadata['prompt_name']}")
        print(f"Transcript: {metadata['transcript_path']}")
        print(f"{'='*70}\n")

    # Load and display summary
    summary_file = result_dir / "summary.md"
    if summary_file.exists():
        with open(summary_file, 'r') as f:
            print(f.read())

def compare_results(test_ids):
    """Compare multiple test results side-by-side."""
    results = []

    for test_id in test_ids:
        result_dir = SUMMARIES_DIR / test_id

        metadata_file = result_dir / "metadata.json"
        summary_file = result_dir / "summary.md"

        if metadata_file.exists() and summary_file.exists():
            with open(metadata_file, 'r') as f:
                metadata = json.load(f)

            with open(summary_file, 'r') as f:
                summary_text = f.read()

            results.append({
                "test_id": test_id,
                "prompt_name": metadata["prompt_name"],
                "timestamp": metadata["timestamp"],
                "summary": summary_text
            })

    if not results:
        print("No test results found to compare.")
        return

    # Create comparison output
    output = Path("COMPARISON.md")

    with open(output, 'w') as f:
        f.write("# Summary Comparison\n\n")
        f.write(f"Comparison generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for i, result in enumerate(results, 1):
            f.write(f"## {i}. {result['prompt_name']} ({result['timestamp']})\n\n")
            f.write(f"Test ID: `{result['test_id']}`\n\n")
            f.write(result['summary'])
            f.write("\n\n---\n\n")

    print(f"Comparison saved to: {output}")
    print(f"Compared {len(results)} test results")

def main():
    """Main CLI interface."""

    if len(sys.argv) < 2:
        print("Summary Tester - Generate and compare summaries with different prompts\n")
        print("Usage:")
        print("  python summary_tester.py list                    # List available transcripts")
        print("  python summary_tester.py prompts                 # List available prompts")
        print("  python summary_tester.py generate <transcript_id> <prompt_name>")
        print("  python summary_tester.py results                 # List all test results")
        print("  python summary_tester.py show <test_id>          # Show a test result")
        print("  python summary_tester.py compare <test_id> <test_id> ...")
        print("\nExamples:")
        print("  python summary_tester.py list")
        print("  python summary_tester.py prompts")
        print("  python summary_tester.py generate 0 default")
        print("  python summary_tester.py compare test1_id test2_id")
        return

    command = sys.argv[1]

    if command == "list":
        """List available transcripts."""
        transcripts = find_transcripts()

        if not transcripts:
            print("No transcripts found.")
            return

        print(f"Found {len(transcripts)} transcript(s):\n")
        for i, t in enumerate(transcripts):
            # Try to get readable path
            readable_path = str(t.relative_to(TRANSCRIPTS_DIR) if TRANSCRIPTS_DIR in t.parents else t)
            print(f"  [{i}] {readable_path}")

        print(f"\nUse index number to generate summary: python summary_tester.py generate 0 <prompt_name>")

    elif command == "prompts":
        """List available prompts."""
        prompts = list_available_prompts()

        if not prompts:
            print("No prompts found. Create some in the summary_prompts/ directory")
            return

        print(f"Available prompts ({len(prompts)}):\n")
        for prompt in prompts:
            prompt_file = PROMPTS_DIR / f"{prompt}.md"
            file_size = prompt_file.stat().st_size
            print(f"  • {prompt} ({file_size} bytes)")

    elif command == "generate":
        """Generate a summary."""
        if len(sys.argv) < 4:
            print("Usage: python summary_tester.py generate <transcript_id> <prompt_name>")
            print("\nExample: python summary_tester.py generate 0 default")
            return

        transcript_id = int(sys.argv[2])
        prompt_name = sys.argv[3]

        # Get transcript
        transcripts = find_transcripts()
        if transcript_id >= len(transcripts):
            print(f"Transcript ID {transcript_id} not found. Use 'list' command first.")
            return

        transcript_path = transcripts[transcript_id]

        # Load prompt
        prompt_text = load_prompt(prompt_name)
        if not prompt_text:
            return

        # Generate summary
        summary_text = generate_summary(transcript_path, prompt_text)

        if summary_text:
            # Save result
            test_id, result_dir = save_summary_result(transcript_path, prompt_name, summary_text)

            print(f"\n✓ Summary generated and saved!")
            print(f"Test ID: {test_id}")
            print(f"Location: {result_dir}")
            print(f"\nTo view: python summary_tester.py show {test_id}")
            print(f"Summary preview:\n")
            print(summary_text[:500] + "..." if len(summary_text) > 500 else summary_text)

    elif command == "results":
        """List test results."""
        results = list_test_results()

        if not results:
            print("No test results yet.")
            return

        print(f"Test results ({len(results)}):\n")
        for result in results:
            print(f"  • {result}")

        print(f"\nTo view a result: python summary_tester.py show <test_id>")
        print(f"To compare results: python summary_tester.py compare <test_id1> <test_id2>")

    elif command == "show":
        """Show a test result."""
        if len(sys.argv) < 3:
            print("Usage: python summary_tester.py show <test_id>")
            return

        test_id = sys.argv[2]
        show_test_result(test_id)

    elif command == "compare":
        """Compare multiple test results."""
        if len(sys.argv) < 4:
            print("Usage: python summary_tester.py compare <test_id1> <test_id2> [test_id3] ...")
            print("\nExample: python summary_tester.py compare test1_id test2_id")
            return

        test_ids = sys.argv[2:]
        compare_results(test_ids)

    else:
        print(f"Unknown command: {command}")
        print("Use 'list', 'prompts', 'generate', 'results', 'show', or 'compare'")

if __name__ == "__main__":
    main()
