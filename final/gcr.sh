gcloud builds submit --timeout=900 --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/text_to_image

gcloud run deploy final --image gcr.io/${GOOGLE_CLOUD_PROJECT}/text_to_image --set-env-vars DEZGO_API_KEYS=<API_KEY>  
