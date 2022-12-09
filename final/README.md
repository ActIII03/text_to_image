# Text to Image python flask web app using docker and GCP

# Dependencies
- docker engine 
  - linux docker engine: https://docs.docker.com/engine/install/ubuntu/
  - windows docker engine: https://docs.docker.com/docker-for-windows/install/
  - mac docker engine: https://docs.docker.com/docker-for-mac/install/
- docker compose
  - linux docker compose: https://docs.docker.com/compose/install/
  - windows docker compose: https://docs.docker.com/docker-for-windows/install/
  - mac docker compose: https://docs.docker.com/docker-for-mac/install/

# To get setup
- clone the repo
  * $ git clone git@gitlab:/atouche/cloud-atouche-touche.git
- cd into final directory
  * $ cd final/
- build the docker image
  * $ docker build -t text_to_image .
- run the docker image w/ local_dev script
  * $ ./local_dev.sh
- open a browser and go to http://localhost:8080/

#  Description
- This is a simple python flask web app that takes in a string of text and returns an image render by stability api via a REST API (POST) call.
- The web app is built using the flask framework and is deployed using docker.
- Can see prior generated images at '/' route
