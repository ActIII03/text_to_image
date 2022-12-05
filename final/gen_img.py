from flask import redirect, request, url_for, render_template
from flask.views import MethodView
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

  def post_text():
    """
    Parses text from request form ("text")
    returns response
    """

    text = request.form.get("text")

    url = "https://dezgo.p.rapidapi.com/text2image"

    payload = "steps=65&height=512&sampler=k_lms&width=512&guidance=7.5&prompt=techbro%20working%20at%20FAANG%20Meme%20digital%20art%2C%20highly-detailed%20masterpiece%20trending%20HQ"

    headers = {
      'content-type': 'application/x-www-form-urlencoded',
      'x-rapidapi-key': DEZGO_API_KEYS,
      'x-rapidapi-host': "dezgo.p.rapidapi.com"
    }

    return requests.request("POST", url, data=payload, headers=headers)
