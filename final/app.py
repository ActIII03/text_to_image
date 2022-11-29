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

@app.route("/gen_from_text", methods=["POST"])
def gen_from_text():
  """ 
  Generate image from text POST request
  returns: redirect to homepage
  """
  # get the text from the form
  text = request.form.get("text")

  url = "https://dezgo.p.rapidapi.com/text2image"

  payload = "steps=50&height=512&sampler=k_lms&width=512&guidance=7.5&prompt=an%20astronaut%20riding%20a%20horse%2C%20digital%20art%2C%20highly-detailed%20masterpiece%20trending%20HQ"
  headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'x-rapidapi-key': DEZGO_API_KEYS,
    'x-rapidapi-host': "dezgo.p.rapidapi.com"
  }

  # response = requests.request("POST", url, data=payload, headers=headers)

  # Return png payload from response to "/"
  return redirect("/")


# Error handlers
@app.errorhandler(500)
def server_error(e):
  """
  Return a custom 500 error.
  """ 
 logging.exception("An error occurred during a request.")
 return (
     """
 An internal error occurred: <pre>{}</pre>
 See logs for full stacktrace.
 """.format(
         e
     ),
     500,
    )

# Main function 
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)