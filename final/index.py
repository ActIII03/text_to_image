from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
  def get(self):
    # model = gbmodel.get_model()
    # ai_images = model.select()
    # return render_template("index.html", ai_images=ai_images)
    return render_template("index.html")
