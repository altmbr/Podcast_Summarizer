# Documentation Updates - November 23, 2025

Comprehensive update to CLAUDE.md and README.md to reflect current system state.

## Major Changes

### 1. MLX-Whisper Migration (Cost Savings)

**Updated Documentation:**
- Switched from OpenAI Whisper API to local MLX-Whisper (M1/M2 GPU-accelerated)
- **Transcription now FREE** - previously ~$0.10-0.30 per episode
- Updated cost estimates across all sections
- Added system requirements for M1/M2 Macs

**Files Updated:**
- `.claude/CLAUDE.md` - All transcription references updated
- `README.md` - Data source section updated with MLX-Whisper info

### 2. Current Status Section

Added new "Current Status (November 2025)" section at top of CLAUDE.md:
- ✅ System operational status
- ✅ Recent major updates highlighted
- ✅ Key features summary
- ✅ Cost savings emphasized

### 3. System Requirements

**NEW SECTION** added to CLAUDE.md:
- M1/M2/M3 Mac recommended for GPU acceleration
- macOS 12.0+ for Metal Performance Shaders
- 16GB+ RAM recommended
- Alternative options for non-M1/M2 systems

### 4. Dependencies & API Keys

**Updated sections:**
- Removed OpenAI Whisper from required dependencies
- Marked OPENAI_API_KEY as "legacy/unused"
- Added mlx-whisper as primary dependency
- Clarified only ANTHROPIC_API_KEY is required
- HUGGINGFACE_TOKEN remains optional for pyannote

### 5. Cost Estimates

**Completely revised cost breakdown:**

**OLD (with OpenAI Whisper API):**
- Per episode: ~$0.45-2.00
- Medium usage (50 episodes/month): $22.50-100.00

**NEW (with MLX-Whisper local):**
- Per episode: ~$0.35-1.75 (20-30% savings)
- Medium usage (50 episodes/month): $17.50-87.50
- Heavy usage savings: $20-50/month

**Updated all monthly cost examples** with before/after comparisons.

### 6. Workflow Documentation

**Updated Step 2 (Transcribe):**
- Added MLX-Whisper model info (`mlx-community/whisper-base-mlx`)
- Noted configurable models (tiny, base, small, medium, large)
- Emphasized local processing = no API costs
- M1/M2 GPU acceleration highlighted

### 7. Troubleshooting

**Replaced OpenAI troubleshooting with MLX-Whisper:**
- Removed: "OPENAI_API_KEY not set"
- Removed: "whisper not found"
- Added: "ANTHROPIC_API_KEY not set" (only required key)
- Added: "mlx-whisper not found" with installation steps
- Added: Model caching location info
- Added: M1/M2 requirement note

### 8. License & Attribution

**Updated "Built with" section:**
- Added: MLX-Whisper (Apple MLX framework)
- Added: Anthropic Claude (Haiku 3.5, Sonnet 4.5)
- Added: pyannote.audio
- Removed: OpenAI Whisper API (replaced with GPT-image-1 for header images only)
- Clarified current technology stack

### 9. README.md Updates

**Added Content Generation subsection:**
- Brief overview of Podcast Summarizer backend
- MLX-Whisper, pyannote, Claude Sonnet 4.5 mentioned
- Reference to `.claude/CLAUDE.md` for full details
- Keeps README focused on website while acknowledging backend

## Summary of Benefits

### Cost Savings
- **~20-30% reduction** in per-episode costs
- **$0.10-0.30 saved per episode** on transcription
- **$20-50/month saved** for high-volume users (200 episodes)
- **Total monthly cost** reduced from ~$24.66-108.32 to ~$19.66-95.82 (medium usage)

### Performance
- **Faster transcription** with M1/M2 GPU acceleration
- **No API rate limits** for transcription
- **Offline capability** for transcription step
- **More predictable costs** (only Claude API charges vary)

### System Improvements
- Clearer documentation of requirements
- More accurate cost estimates
- Better troubleshooting guidance
- Updated technology attribution

## Files Modified

1. `.claude/CLAUDE.md` - Comprehensive updates throughout
2. `README.md` - Data source section enhanced
3. `DOCUMENTATION_UPDATES.md` - This summary (NEW)

## Next Steps

**No action required** - Documentation is now up to date with current system.

**Optional future enhancements:**
- Consider documenting fallback to OpenAI API for non-M1/M2 users
- Add performance benchmarks (MLX-Whisper vs OpenAI API)
- Document model size trade-offs (tiny vs base vs large)
- Add troubleshooting for M1/M2 GPU detection issues

---

**Date:** November 23, 2025
**Status:** ✅ Complete
**Impact:** Documentation now accurately reflects cost-optimized MLX-Whisper system
