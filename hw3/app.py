import flask
from flask.views import MethodView
from index import Index
from todo import ToDo

app = flask.Flask(__name__)

app.add_url_rule('/', 
                  view_func=Index.as_view('index'),
                  methods=['GET', 'POST'])

app.add_url_rule('/todo',
                  view_func=ToDo.as_view('todo'),
                  methods=['GET', 'POST'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)