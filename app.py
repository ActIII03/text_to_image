import flask, os
from flask.views import MethodView
from index import Index
from gen_img import GenImg

app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/gen_from_text',
                  view_func=GenImg.as_view('post'),
                  methods=["POST"])

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=int(os.environ.get('PORT',8080)), debug=True)
