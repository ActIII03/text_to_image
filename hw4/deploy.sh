#!/bin/bash -e

# Build using Cloud Build
# gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/gcp_gb

# Deploy 
gcloud run deploy hw4 \
  --image gcr.io/${GOOGLE_CLOUD_PROJECT}/gcp_todo \
  --service-account todo-app@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com