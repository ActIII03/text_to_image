from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import os
import requests

import gbmodel

class GenImg(MethodView):
  def post(self):
    """
    Accepts POST request and process the form;
    redirects to index when done
    """
    model = gbmodel.get_model()
    # Call post_text() to get the image from the API
    response = self.post_text()
    model.insert(response.content, request.form['text_prompt'])
    return redirect(url_for('index'))

  def post_text(self):
    """
    Parses text from request form ("text")
    returns response
    """

    text_prompt = request.form.get("text_prompt")
    #replace spaces with %20
    text_prompt = text_prompt.replace(" ", "%20")
    # replace commas with %2C
    text_prompt = text_prompt.replace(",", "%2C")
    # replace periods with %2E
    text_prompt = text_prompt.replace(".", "%2E")


    url = "https://dezgo.p.rapidapi.com/text2image"

    payload = "steps=65&height=512&sampler=k_lms&width=512&guidance=7.5&prompt=" + text_prompt + "%20HQ"

    headers = {
      'content-type': 'application/x-www-form-urlencoded',
      'x-rapidapi-key': os.environ.get("DEZGO_API_KEYS"),
      'x-rapidapi-host': "dezgo.p.rapidapi.com"
    }

    return requests.request("POST", url, data=payload, headers=headers)
