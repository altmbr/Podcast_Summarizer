#!/bin/bash
# Deploy all Cloud Functions for the podcast transcription system

set -e

# Configuration
PROJECT_ID="gen-lang-client-0111593271"
REGION="us-central1"
SA_EMAIL="podcast-processor@${PROJECT_ID}.iam.gserviceaccount.com"
GCS_BUCKET="${PROJECT_ID}-podcast-data"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}Deploying Cloud Functions for Podcast Transcription System${NC}"
echo "Project: $PROJECT_ID"
echo "Region: $REGION"
echo ""

# Check if we're in the right directory
if [ ! -d "cloud/functions/discovery" ]; then
    echo -e "${RED}Error: Must run from project root (where cloud/ directory exists)${NC}"
    exit 1
fi

cd cloud

# Deploy Discovery Function
echo -e "${GREEN}[1/2] Deploying discovery function...${NC}"
gcloud functions deploy discovery \
  --gen2 \
  --runtime python311 \
  --region $REGION \
  --source functions/discovery \
  --entry-point discovery \
  --trigger-http \
  --allow-unauthenticated \
  --service-account $SA_EMAIL \
  --set-secrets "SENDGRID_API_KEY=SENDGRID_API_KEY:latest" \
  --set-env-vars "GCS_BUCKET=${GCS_BUCKET},TEST_MODE=true,TEST_EMAIL=altmbr@gmail.com"

echo ""

# Deploy Webhook Function
echo -e "${GREEN}[2/2] Deploying email-reply-webhook function...${NC}"
gcloud functions deploy email-reply-webhook \
  --gen2 \
  --runtime python311 \
  --region $REGION \
  --source functions/webhook \
  --entry-point webhook \
  --trigger-http \
  --allow-unauthenticated \
  --service-account $SA_EMAIL \
  --set-env-vars "GCS_BUCKET=${GCS_BUCKET},GCP_PROJECT=${PROJECT_ID},GCP_REGION=${REGION},AUTHORIZED_EMAILS=altmbr@gmail.com,TEST_MODE=true"

echo ""
echo -e "${GREEN}✓ All functions deployed successfully!${NC}"
echo ""
echo "Test endpoints:"
echo "  Discovery: https://us-central1-${PROJECT_ID}.cloudfunctions.net/discovery"
echo "  Webhook:   https://us-central1-${PROJECT_ID}.cloudfunctions.net/email-reply-webhook"
