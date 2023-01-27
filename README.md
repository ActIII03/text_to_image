# Text to Image python flask web app using docker and GCP Cloud Run

# Dependencies
- docker engine 
  - linux docker engine: https://docs.docker.com/engine/install/ubuntu/
  - windows docker engine: https://docs.docker.com/docker-for-windows/install/
  - mac docker engine: https://docs.docker.com/docker-for-mac/install/
- docker compose
  - linux docker compose: https://docs.docker.com/compose/install/
  - windows docker compose: https://docs.docker.com/docker-for-windows/install/
  - mac docker compose: https://docs.docker.com/docker-for-mac/install/
- virtualenv (if you want to run in venv): https://virtualenv.pypa.io/en/latest/installation.html

# Pre-requisites
- GCP account
- RapidAPI account and API key via [Dzego](https://rapidapi.com/dzego/api/dzego)
- Set env vars for API:
  - $ export RAPIDAPI_KEY=<your_rapidapi_key>
- GCP env vars:
  - $ export GOOGLE_CLOUD_PROJECT=<your_gcp_project_id>
- Afterwards, run get_creds.sh to get GCP credentials
  - $ ./script/get_creds.sh
# To get setup
* Note:  If you want to run in a virtual environment, run the following commands:
  - $ virtualenv venv
  - $ source venv/bin/activate
  - $ pip install -r requirements.txt
  - $ flask run

* Docker setup:
  - clone the repo
    * $ git clone git@github.com:/ActIII03/text_to_image.git
  - cd into text_to_image directory
  - build the docker image
    * $ docker build -t text_to_image .
  - run the docker image w/ local_dev script
    * $ ./script/local_dev.sh
  - open a browser and go to http://localhost:8080/

#  Description
- This is a simple python flask web app that takes in a string of text and returns an image render by stability api via a REST API (POST) call.
- The web app is built using the flask framework and is deployed using docker container on GCP Cloud Run
- Can see prior generated images at '/' route

# Deployment
- Unfortunately, this was a school project but does utilizes GCP's Cloud Run which requires GCP account with billing enabled.
