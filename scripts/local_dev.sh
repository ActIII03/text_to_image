#!/bin/bash

# Local docker dev env 
cd ../
docker run -p 8080:8080 --env PORT=8080 -v $GOOGLE_APPLICATION_CREDENTIALS:/tmp/keys/FILE_NAME.json:ro -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/FILE_NAME.json -e DEZGO_API_KEYS=<API_KEYS> --rm text_to_image
