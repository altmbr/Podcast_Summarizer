# GCP Cloud Functions Setup Guide

## Initial Setup (One-time)

This guide walks through setting up gcloud SDK on your local machine for deploying Cloud Functions.

## Prerequisites

- macOS, Linux, or Windows with WSL2
- `curl` installed
- Terminal access
- GCP project access (gen-lang-client-0111593271)

## Step 1: Install gcloud SDK

### macOS (recommended method)
```bash
# Install via official installer
curl https://sdk.cloud.google.com | bash -s -- --disable-prompts --install-dir=$HOME

# Restart shell to load gcloud
exec -l $SHELL

# Verify installation
~/google-cloud-sdk/bin/gcloud --version
```

### Alternative: Homebrew (simpler but may have permissions issues)
```bash
brew install google-cloud-sdk

# Add to PATH
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Linux
```bash
# Download and install
curl https://sdk.cloud.google.com | bash

# Initialize
gcloud init
```

### Fix Permissions (if needed)
If you get permission errors on `~/.config`:
```bash
sudo chown -R $USER:staff ~/.config
```

## Step 2: Authenticate with GCP

### Option A: User Account (Interactive - Recommended)
```bash
# This will open a browser for authentication
~/google-cloud-sdk/bin/gcloud auth login

# Set project
~/google-cloud-sdk/bin/gcloud config set project gen-lang-client-0111593271

# Verify authentication
~/google-cloud-sdk/bin/gcloud auth list
~/google-cloud-sdk/bin/gcloud config list
```

### Option B: Service Account (Non-interactive)
```bash
# Download service account key from GCP Console
# Then authenticate:
gcloud auth activate-service-account \
  --key-file=/path/to/service-account-key.json

gcloud config set project gen-lang-client-0111593271
```

## Step 3: Add gcloud to PATH (Optional but recommended)

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):
```bash
export PATH="$HOME/google-cloud-sdk/bin:$PATH"
```

Then reload:
```bash
source ~/.zshrc  # or ~/.bashrc
```

After this, you can use `gcloud` instead of `~/google-cloud-sdk/bin/gcloud`.

## Step 4: Verify Setup

Run these commands to verify everything is working:
```bash
# Check version
gcloud --version

# Check authenticated account
gcloud auth list

# Check current project
gcloud config get-value project

# List Cloud Functions (should show existing functions)
gcloud functions list --gen2 --region us-central1
```

Expected output:
```
✓ gcloud version 400+
✓ Authenticated as: altmbr@gmail.com
✓ Project: gen-lang-client-0111593271
✓ Functions: discovery, email-reply-webhook
```

## Troubleshooting

### Command not found: gcloud
**Problem:** gcloud not in PATH

**Solution:**
```bash
# Use full path
~/google-cloud-sdk/bin/gcloud --version

# Or add to PATH
export PATH="$HOME/google-cloud-sdk/bin:$PATH"
```

### Python 3.9 deprecation warning
**Problem:** Warning about Python 3.9

**Solution:** This is just a warning. You can:
1. Ignore it (works until Jan 2026)
2. Install Python 3.10+ and set `CLOUDSDK_PYTHON` env var
3. Run `gcloud components reinstall` to get bundled Python

### Permission denied on ~/.config
**Problem:** Cannot create config files

**Solution:**
```bash
sudo chown -R $(whoami):staff ~/.config
```

### Authentication failed
**Problem:** Browser authentication fails

**Solution:**
```bash
# Use no-browser mode and manually paste the URL
gcloud auth login --no-launch-browser
```

### Wrong project selected
**Problem:** Commands affect wrong project

**Solution:**
```bash
# Always verify current project
gcloud config get-value project

# Change if needed
gcloud config set project gen-lang-client-0111593271
```

## What's Next?

After setup is complete, you can:
- Deploy functions using the examples in SKILL.md
- View logs: `gcloud functions logs read FUNCTION_NAME --gen2 --region us-central1`
- Test endpoints: `curl https://us-central1-gen-lang-client-0111593271.cloudfunctions.net/discovery`
- Update function code and redeploy instantly

## Cost Considerations

- Cloud Functions (Gen 2): ~$0.40/million requests
- Cloud Build: First 120 builds/day free
- Secret Manager: First 6 secrets free
- Cloud Storage: $0.02/GB/month
- Typical monthly cost: < $5 for this workload
