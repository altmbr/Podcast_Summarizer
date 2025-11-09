# Speaker Diarization Setup Guide

## Issue
The pyannote speaker diarization models are "gated" on HuggingFace, which means you need to accept terms of use before you can download them.

## Setup Steps

### 1. Accept Model Terms (One-time)

You need to accept the terms for these models:

1. **Main diarization model:** Visit https://huggingface.co/pyannote/speaker-diarization-3.1
   - Click "Agree and access repository"
   - Accept the terms

2. **Segmentation model:** Visit https://huggingface.co/pyannote/segmentation-3.0
   - Click "Agree and access repository"
   - Accept the terms

### 2. Verify Your HuggingFace Token

1. Go to https://huggingface.co/settings/tokens
2. Make sure you have a token with **READ** access
3. Copy the token
4. Add it to your `.env` file:
   ```
   HUGGINGFACE_TOKEN=hf_your_token_here
   ```

### 3. Re-run the Test

After accepting the terms, wait 5-10 minutes for HuggingFace to update your permissions, then run:

```bash
python3 test_diarization.py
```

## Alternative: Skip Diarization

If you don't want to use speaker diarization, you can still use the system without it. The script will:
1. Transcribe the audio without speaker labels
2. Use Claude to try to identify speakers from context alone (less accurate)

## How It Works

Once properly configured:

1. **Voice Analysis**: pyannote analyzes the audio waveform to detect different voices
2. **Speaker Labels**: Assigns labels like SPEAKER_00, SPEAKER_01 based on voice characteristics
3. **Name Identification**: Claude AI analyzes the transcript to replace SPEAKER_XX with actual names
4. **Final Output**: Transcript with speaker names instead of generic labels

## Expected Output

After accepting terms, you should see:

```
✓ Diarization complete!

DETECTED SPEAKERS SUMMARY:
SPEAKER_00: 1245.3s (20.8 minutes)
SPEAKER_01: 892.1s (14.9 minutes)
```

Then the transcript will show:
```
[00:00:15] SPEAKER_00: So David, you've been at Sequoia for quite some time now.
[00:00:22] SPEAKER_01: Yes, I joined about five years ago...
```

Later, Claude will replace SPEAKER_00 with "Harry" and SPEAKER_01 with "David" based on context.
