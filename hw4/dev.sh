#!/bin/bash -e

# build gcp_todo docker image
# docker build -t gcp_todo .

# Run docker locally and mount GOOGLE_APPLICATION_CREDENTIALS to container volume
docker run -v $GOOGLE_APPLICATION_CREDENTIALS:/tmp/keys/todo-app.json:ro --env GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/todo-app.json -p 8080:8080 --env PORT=8080 --rm gcp_todo:latest