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
echo "Step 1/7: Building Docker image..."
cd "$(dirname "$0")/.."
gcloud builds submit \
  --tag "${REGION}-docker.pkg.dev/${PROJECT_ID}/podcast-summarizer/processor:latest" \
  --timeout=30m \
  --project $PROJECT_ID

echo "✓ Docker image built and pushed"

# Step 2: Deploy Cloud Run Job (CPU for now, GPU when approved)
echo ""
echo "Step 2/7: Deploying Cloud Run Job..."
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
echo "Step 3/7: Deploying Discovery Function..."
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
echo "Step 4/7: Deploying Webhook Function..."
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
echo "Step 5/7: Creating Cloud Scheduler (Discovery)..."
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

echo "✓ Cloud Scheduler created (Discovery)"

# Step 6: Deploy Podscan Processor Function
echo ""
echo "Step 6/7: Deploying Podscan Processor Function..."
gcloud functions deploy podscan-processor \
  --gen2 \
  --runtime python311 \
  --region $REGION \
  --project $PROJECT_ID \
  --source functions/podscan_processor \
  --entry-point podscan_processor \
  --trigger-http \
  --allow-unauthenticated \
  --timeout 3600 \
  --memory 512Mi \
  --service-account $SA_EMAIL \
  --set-secrets "PODSCAN_API_KEY=PODSCAN_API_KEY:latest,ANTHROPIC_API_KEY=ANTHROPIC_API_KEY:latest,GITHUB_TOKEN=GITHUB_TOKEN:latest,SENDGRID_API_KEY=SENDGRID_API_KEY:latest" \
  --set-env-vars "NOTIFICATION_EMAIL=altmbr@gmail.com,LOOKBACK_DAYS=3"

echo "✓ Podscan Processor Function deployed"

# Step 7: Create Cloud Scheduler for Podscan (1 PM EST daily)
echo ""
echo "Step 7/7: Creating Cloud Scheduler (Podscan)..."
gcloud scheduler jobs create http podscan-daily \
  --location $REGION \
  --project $PROJECT_ID \
  --schedule "0 13 * * *" \
  --time-zone "America/New_York" \
  --uri "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/podscan-processor" \
  --http-method GET \
  --oidc-service-account-email $SA_EMAIL \
  --oidc-token-audience "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/podscan-processor" \
  || gcloud scheduler jobs update http podscan-daily \
    --location $REGION \
    --project $PROJECT_ID \
    --schedule "0 13 * * *" \
    --time-zone "America/New_York"

echo "✓ Cloud Scheduler created (Podscan)"

# Step 8: Deploy Paper Processor Function
echo ""
echo "Step 8/9: Deploying Paper Processor Function..."
gcloud functions deploy paper-processor \
  --gen2 \
  --runtime python311 \
  --region $REGION \
  --project $PROJECT_ID \
  --source functions/paper_processor \
  --entry-point paper_processor \
  --trigger-http \
  --allow-unauthenticated \
  --timeout 900 \
  --memory 512Mi \
  --service-account $SA_EMAIL \
  --set-secrets "ANTHROPIC_API_KEY=ANTHROPIC_API_KEY:latest,GITHUB_TOKEN=GITHUB_TOKEN:latest,AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID:latest,AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY:latest" \
  --set-env-vars "NOTIFICATION_EMAIL=altmbr@gmail.com,PAPER_LOOKBACK_DAYS=3"

echo "✓ Paper Processor Function deployed"

# Step 9: Create Cloud Scheduler for Papers (5 AM EST daily)
echo ""
echo "Step 9/9: Creating Cloud Scheduler (Paper Processor)..."
gcloud scheduler jobs create http paper-daily \
  --location $REGION \
  --project $PROJECT_ID \
  --schedule "0 5 * * *" \
  --time-zone "America/New_York" \
  --uri "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/paper-processor" \
  --http-method GET \
  --oidc-service-account-email $SA_EMAIL \
  --oidc-token-audience "https://${REGION}-${PROJECT_ID}.cloudfunctions.net/paper-processor" \
  || gcloud scheduler jobs update http paper-daily \
    --location $REGION \
    --project $PROJECT_ID \
    --schedule "0 5 * * *" \
    --time-zone "America/New_York"

echo "✓ Cloud Scheduler created (Paper Processor)"

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
echo "Test podscan processor (dry run):"
echo "curl 'https://${REGION}-${PROJECT_ID}.cloudfunctions.net/podscan-processor?dry_run=true'"
echo ""
echo "Test paper processor (dry run):"
echo "curl 'https://${REGION}-${PROJECT_ID}.cloudfunctions.net/paper-processor?dry_run=true'"
echo ""
echo "REQUIRED: Add PODSCAN_API_KEY to Secret Manager:"
echo "echo -n 'your-api-key' | gcloud secrets create PODSCAN_API_KEY --data-file=- --project $PROJECT_ID"
echo ""
