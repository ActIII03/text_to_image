"""
Simple Text to image generator application using Flask (MVC pattern) where the users' queries are converted to images and stored in Google Datastore.
"""
from datetime import datetime
from config import *
import logging
import os
import requests

from flask import Flask, redirect, render_template, request

from google.cloud import datastore
from google.cloud import storage

# dev imports
import io

app = Flask(__name__)

@app.route("/")
def homepage():
  """
  Homepage of the application
  returns: rendered homepage.html
  """ 
  # create datastore client
  # datastore_client = datastore.Client()

  # query for all entities for imageAI
  # query = datastore_client.query(kind="imageAI")
  # ai_images = list(query.fetch())

  ai_images = []

  return render_template("homepage.html", ai_images=ai_images)

def post_text():
  """
  Parses text from request form ("text")
  returns response
  """
  # get the text from the form
  text = request.form.get("text")

  url = "https://dezgo.p.rapidapi.com/text2image"

  payload = "steps=65&height=512&sampler=k_lms&width=512&guidance=7.5&prompt=schrodinger%20cat%20laying%20in%20laundry%20masterpiece%20trending%20HQ"
  headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'x-rapidapi-key': DEZGO_API_KEYS,
    'x-rapidapi-host': "dezgo.p.rapidapi.com"
  }

  # return requests.request("POST", url, data=payload, headers=headers)

def post_image(img):
  """
  Uploads image to Google Cloud Storage
  args: img
  returns: response[imgUrl, imgName, textPrompt]
  """

  # create storage client
  storage_client = storage.Client()

  # get bucket
  bucket = storage_client.get_bucket(GCS_BUCKET)







@app.route("/gen_from_text", methods=["POST"])
def gen_from_text():
  """ 
  Generate image from text POST request
  returns: redirect to homepage
  """
  response = post_text()

  # dev code block DELETE Later

  # open png file from test_img/ 
  with open("test_img/test.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
  # END of dev block
    
  # call put_image() to store image in Google Datastore passing in png file
  put_image(encoded_string)

  # Return png payload from response to "/"
  return redirect("/")

# Main function 
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)