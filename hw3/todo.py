from flask import redirect, url_for, request, render_template
from flask.views import MethodView
import gbmodel

class ToDo(MethodView):
    def get(self: "ToDo") -> "flask.Response":
        """
        Displays the todo page
        :return: The todo page
        """
        return render_template('todo.html')

    def post(self: "ToDo") -> "flask.Response":
        """
        Adds a new task to the database
        :return: Redirects to the todo page
        """
        model = gbmodel.get_model()
        model.insert(request.form['task'], request.form['due_date'], request.form['description'])
        return redirect(url_for('index'))

    def delete(self: "ToDo") -> "flask.Response":
        """
        Deletes a task from the database
        :return: Redirects to the todo page
        """
        model = gbmodel.get_model()
        model.delete(request.form['task'])
        return redirect(url_for('index'))