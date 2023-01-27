# Script to create a new google cloud role and generate a key (json file)
# Assumes you have gcloud sdk installed and configured

# Set the project name
PROJECT_NAME=<PROJECT_NAME>

# Set the role name
ROLE_NAME=<ROLE_NAME>

# Create the role w/ datastore access (roles/datastore.user), storage access (roles/storage.objectAdmin)
gcloud iam service-accounts create $ROLE_NAME --display-name $ROLE_NAME --project $PROJECT_NAME

# Create a key for the role
 gcloud iam service-accounts keys create $ROLE_NAME.json --iam-account $ROLE_NAME@$PROJECT_NAME.iam.gserviceaccount.com
 
# Grant the role access to the project
gcloud projects add-iam-policy-binding $PROJECT_NAME --member serviceAccount:$ROLE_NAME@$PROJECT_NAME.iam.gserviceaccount.com --role roles/datastore.owner --role roles/storage.objectAdmin
 
# Download the key as a json file
gcloud iam service-accounts keys create $ROLE_NAME.json --iam-account $ROLE_NAME@$PROJECT_NAME.iam.gserviceaccount.com

# Set the environment variable
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/$ROLE_NAME.json
# 

# Add storage.buckets.get access to the role
gcloud projects add-iam-policy-binding $PROJECT_NAME --member serviceAccount:$ROLE_NAME@$PROJECT_NAME.iam.gserviceaccount.com --role roles/storage.objectViewer
