# Small docker image for python flask app
FROM google/cloud-sdk

LABEL maintainer="atouche@pdx.edu"

WORKDIR /app

COPY requirements.txt  .

COPY . .

RUN apt update -y && \
  apt install -y python3-pip && \
  pip3 install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
