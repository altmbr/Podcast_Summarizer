---
name: gcp-cloud-functions
description: Install gcloud SDK, authenticate with GCP, deploy Cloud Functions to Google Cloud Platform, and troubleshoot deployment issues. Use when deploying serverless functions, setting up gcloud authentication, updating Cloud Functions, or debugging GCP deployment problems.
allowed-tools: Read, Bash, Edit, Write
---

# GCP Cloud Functions Deployment Skill

## Overview

This skill helps you manage Google Cloud Functions deployments for the podcast transcription system. It handles:
- Installing and configuring gcloud SDK
- Authenticating with GCP project `gen-lang-client-0111593271`
- Deploying Cloud Functions (discovery, webhook, processor)
- Troubleshooting common deployment issues

## Project Configuration

**GCP Project:** gen-lang-client-0111593271
**Region:** us-central1
**Service Account:** podcast-processor@gen-lang-client-0111593271.iam.gserviceaccount.com
**GCS Bucket:** gen-lang-client-0111593271-podcast-data

## Quick Reference

### Deploy Discovery Function
```bash
cd cloud
gcloud functions deploy discovery \
  --gen2 \
  --runtime python311 \
  --region us-central1 \
  --source functions/discovery \
  --entry-point discovery \
  --trigger-http \
  --allow-unauthenticated \
  --service-account podcast-processor@gen-lang-client-0111593271.iam.gserviceaccount.com \
  --set-secrets "SENDGRID_API_KEY=SENDGRID_API_KEY:latest" \
  --set-env-vars "GCS_BUCKET=gen-lang-client-0111593271-podcast-data,TEST_MODE=true,TEST_EMAIL=altmbr@gmail.com"
```

### Deploy Webhook Function
```bash
cd cloud
gcloud functions deploy email-reply-webhook \
  --gen2 \
  --runtime python311 \
  --region us-central1 \
  --source functions/webhook \
  --entry-point webhook \
  --trigger-http \
  --allow-unauthenticated \
  --service-account podcast-processor@gen-lang-client-0111593271.iam.gserviceaccount.com \
  --set-env-vars "GCS_BUCKET=gen-lang-client-0111593271-podcast-data,GCP_PROJECT=gen-lang-client-0111593271,GCP_REGION=us-central1,AUTHORIZED_EMAILS=altmbr@gmail.com,TEST_MODE=true"
```

### Test Function
```bash
# Test discovery function
curl -s "https://us-central1-gen-lang-client-0111593271.cloudfunctions.net/discovery"

# Test webhook function (requires SendGrid payload format)
curl -X POST "https://us-central1-gen-lang-client-0111593271.cloudfunctions.net/email-reply-webhook" \
  -H "Content-Type: application/json" \
  -d '{"from":"altmbr@gmail.com","text":"all"}'
```

### View Logs
```bash
gcloud functions logs read discovery --gen2 --region us-central1 --limit 50
gcloud functions logs read email-reply-webhook --gen2 --region us-central1 --limit 50
```

## Deployment Workflow

When deploying functions from local machine:

1. **Edit function code locally** using standard tools (Edit, Write)
2. **Deploy directly** using gcloud CLI (already authenticated)
3. **Test endpoint** using curl
4. **Check logs** if issues arise
5. **Commit changes** to git after successful deployment

## Setup Instructions

See [setup-guide.md](setup-guide.md) for detailed installation and authentication steps.

## Common Issues

### gcloud command not found
**Solution:** The gcloud SDK is installed at `~/google-cloud-sdk/bin/gcloud`. Add to PATH:
```bash
export PATH="$HOME/google-cloud-sdk/bin:$PATH"
```

### Python 3.9 deprecation warning
**Note:** This is just a warning. gcloud SDK will continue working until Jan 2026. Can be safely ignored.

### Permission denied errors
**Solution:** Verify service account has necessary IAM roles:
- Cloud Functions Developer
- Cloud Run Admin
- Service Account User
- Secret Manager Secret Accessor

### Deployment timeout
**Solution:** Cloud Function deployments can take 3-5 minutes. Use `--timeout=300` or wait patiently.

### Function shows old code after deployment
**Solution:** Check the deployment output for the new revision number. It may take 30-60 seconds for traffic to shift to new revision.

## Environment Variables

**Discovery Function:**
- `GCS_BUCKET`: Cloud Storage bucket name
- `TEST_MODE`: Set to "true" for testing
- `TEST_EMAIL`: Email address for test notifications
- `SENDGRID_API_KEY`: (secret) SendGrid API key for sending emails

**Webhook Function:**
- `GCS_BUCKET`: Cloud Storage bucket name
- `GCP_PROJECT`: GCP project ID
- `GCP_REGION`: GCP region
- `AUTHORIZED_EMAILS`: Comma-separated list of authorized sender emails
- `TEST_MODE`: Set to "true" for testing

## File Locations

- **Local project:** `/Users/bryanaltman/Documents/Transcription Playground/cloud/`
- **Discovery function:** `cloud/functions/discovery/main.py`
- **Webhook function:** `cloud/functions/webhook/main.py`
- **gcloud config:** `~/.config/gcloud/`
- **gcloud binary:** `~/google-cloud-sdk/bin/gcloud`

## Tips

- Always work from the project root when deploying
- Use `--no-launch-browser` flag for non-interactive authentication
- Test functions locally first if possible
- Keep TEST_MODE=true until ready for production
- Monitor costs via GCP Console Billing page
