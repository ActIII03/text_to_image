from flask import redirect, url_for, request, render_template
from flask.views import MethodView
from datetime import datetime
import gbmodel

class ToDo(MethodView):
    def get(self):
        """
        Displays the todo page
        :return: The todo page
        """
        return render_template('todo.html')

    def post(self):
        """
        Adds a new task to the database
        :return: Redirects to the todo page
        """
        model = gbmodel.get_model()
        model.insert(request.form['task'], datetime.now(), request.form['due_date'], request.form['description'])
        return redirect(url_for('index'))

    def delete(self):
        """
        Deletes a task from the database
        :return: Redirects to the todo page
        """
        model = gbmodel.get_model()
        model.delete(request.form['task'])
        return redirect(url_for('index'))