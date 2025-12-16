#!/bin/bash
# Deploy all components to Google Cloud Platform
# Run from cloud/ directory

set -e  # Exit on error

PROJECT_ID="${GCP_PROJECT:-gen-lang-client-0111593271}"
REGION="us-central1"
SA_EMAIL="podcast-processor@${PROJECT_ID}.iam.gserviceaccount.com"

echo "================================================"
echo "Deploying Podcast Summarizer to GCP"
echo "Project: $PROJECT_ID"
echo "Region: $REGION"
echo "================================================"
echo ""

# Step 1: Build and push Docker image
echo "Step 1/5: Building Docker image..."
cd "$(dirname "$0")/.."
gcloud builds submit \
  --tag "${REGION}-docker.pkg.dev/${PROJECT_ID}/podcast-summarizer/processor:latest" \
  --timeout=30m \
  --project $PROJECT_ID

echo "✓ Docker image built and pushed"

# Step 2: Deploy Cloud Run Job (CPU for now, GPU when approved)
echo ""
echo "Step 2/5: Deploying Cloud Run Job..."
gcloud run jobs create podcast-processor \
  --image "${REGION}-docker.pkg.dev/${PROJECT_ID}/podcast-summarizer/processor:latest" \
  --region $REGION \
  --project $PROJECT_ID \
  --cpu 4 \
  --memory 16Gi \
  --max-retries 1 \
  --task-timeout 180m \
  --service-account $SA_EMAIL \
  --set-secrets "ANTHROPIC_API_KEY=ANTHROPIC_API_KEY:latest,HUGGINGFACE_TOKEN=HUGGINGFACE_TOKEN:latest,GITHUB_TOKEN=GITHUB_TOKEN:latest,EVOMI_PROXY_USERNAME=EVOMI_PROXY_USERNAME:latest,EVOMI_PROXY_PASSWORD=EVOMI_PROXY_PASSWORD:latest" \
  --set-env-vars "GCS_BUCKET=${PROJECT_ID}-podcast-data,GCP_PROJECT=${PROJECT_ID}" \
  || gcloud run jobs update podcast-processor \
    --image "${REGION}-docker.pkg.dev/${PROJECT_ID}/podcast-summarizer/processor:latest" \
    --region $REGION \
    --project $PROJECT_ID \
    --set-secrets "ANTHROPIC_API_KEY=ANTHROPIC_API_KEY:latest,HUGGINGFACE_TOKEN=HUGGINGFACE_TOKEN:latest,GITHUB_TOKEN=GITHUB_TOKEN:latest,EVOMI_PROXY_USERNAME=EVOMI_PROXY_USERNAME:latest,EVOMI_PROXY_PASSWORD=EVOMI_PROXY_PASSWORD:latest" \
    --set-env-vars "GCS_BUCKET=${PROJECT_ID}-podcast-data,GCP_PROJECT=${PROJECT_ID}"

echo "✓ Cloud Run Job deployed"

# Step 3: Deploy Discovery Function
echo ""
echo "Step 3/5: Deploying Discovery Function..."
gcloud functions deploy discovery \
  --gen2 \
  --runtime python311 \
  --region $REGION \
  --project $PROJECT_ID \
  --source functions/discovery \
  --entry-point discovery \
  --trigger-http \
  --allow-unauthenticated \
  --service-account $SA_EMAIL \
  --set-secrets "SENDGRID_API_KEY=SENDGRID_API_KEY:latest" \
  --set-env-vars "GCS_BUCKET=${PROJECT_ID}-podcast-data,TEST_MODE=true,TEST_EMAIL=altmbr@gmail.com"

echo "✓ Discovery Function deployed"

# Step 4: Deploy Webhook Function
echo ""
echo "Step 4/5: Deploying Webhook Function..."
gcloud functions deploy email-reply-webhook \
  --gen2 \
  --runtime python311 \
  --region $REGION \
  --project $PROJECT_ID \
  --source functions/webhook \
  --entry-point webhook \
  --trigger-http \
  --allow-unauthenticated \
  --service-account $SA_EMAIL \
  --set-env-vars "GCS_BUCKET=${PROJECT_ID}-podcast-data,GCP_PROJECT=${PROJECT_ID},GCP_REGION=${REGION},AUTHORIZED_EMAILS=altmbr@gmail.com,TEST_MODE=true"

echo "✓ Webhook Function deployed"

# Step 5: Create Cloud Scheduler (1 PM EST)
echo ""
echo "Step 5/5: Creating Cloud Scheduler..."
gcloud scheduler jobs create http podcast-discovery \
  --location $REGION \
  --project $PROJECT_ID \
  --schedule "0 13 * * *" \
  --time-zone "America/New_York" \
  --uri "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/discovery" \
  --http-method GET \
  --oidc-service-account-email $SA_EMAIL \
  --oidc-token-audience "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/discovery" \
  || gcloud scheduler jobs update http podcast-discovery \
    --location $REGION \
    --project $PROJECT_ID \
    --schedule "0 13 * * *" \
    --time-zone "America/New_York"

echo "✓ Cloud Scheduler created"

echo ""
echo "================================================"
echo "✓ Deployment complete!"
echo "================================================"
echo ""
echo "IMPORTANT: Configure SendGrid Inbound Parse webhook URL:"
echo "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/email-reply-webhook"
echo ""
echo "Test discovery function:"
echo "curl https://${REGION}-${PROJECT_ID}.cloudfunctions.net/discovery"
echo ""
