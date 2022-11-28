#!/bin/bash

# Local docker dev env 
docker run -p 8080:8080 --env PORT=8080 --rm text_to_image
