# Small docker image for python flask app
<<<<<<< HEAD
FROM google/cloud-sdk

LABEL maintainer="atouche@pdx.edu"

WORKDIR /app

COPY requirements.txt  .

COPY . .

RUN apt update -y && \
  apt install -y python3-pip && \
  pip3 install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
=======
FROM python:3.8-alpine 

WORKDIR /app

COPY requirements.txt  /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
>>>>>>> origin/main
