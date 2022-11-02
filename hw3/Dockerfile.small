# Small docker image for python flask app
FROM python:3.8-alpine 

WORKDIR /app

COPY requirements.txt  /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
