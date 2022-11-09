#!/bin/bash -e

# config gcloud project config
gcloud config set project <PROJECT_ID>

# create Datastore region=us-west1
gcloud datastore databases create --region=us-west1

# create SErvice account for to-do app (IAM) called todo-app 
gcloud iam service-accounts create todo-app

# assign role of role/datastore.user to todo-app
gcloud projects add-iam-policy-binding $(gcloud config get-value project) \
  --member serviceAccount:todo-app@$(gcloud config get-value project).iam.gserviceaccount.com \
  --role roles/datastore.user
#
## list service accounts for project
gcloud iam service-accounts list
#
## download JSON key for todo-app  serviceAccount:todo-app@hw4-todo-368106.iam.gserviceaccount.com
gcloud iam service-accounts keys create todo-app.json \
    --iam-account=todo-app@$(gcloud config get-value project).iam.gserviceaccount.com

# Move json key to ~/Downloads/
mv todo-app.json ~/Downloads/

# Export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/todo-app.json
export GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/todo-app.json