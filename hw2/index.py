from flask import render_template
from flask.views import MethodView
# import from local directory called gbmodel
import gbmodel

class Index(MethodView):
    def get(self: "Index") -> "flask.Response":
        """
        Displays the index page
        :return: The index page
        """
        model = gbmodel.get_model()
        tasks = [dict(task=row[0], date=row[1], due_date=row[2], description=row[3]) for row in model.select()]
        return render_template('index.html', tasks=tasks)