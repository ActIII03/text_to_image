from .Model import Model
from datetime import date
import sqlite3

DB_FILE = 'tasks.db' # file for database

class model(Model):
  def __init__(self: "model") -> None:
    """
    Initializes the database if it does not exist
    :return: none
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    try:
      cursor.execute("SELECT count(*) FROM tasks")
    except sqlite3.OperationalError:
      cursor.execute("CREATE TABLE tasks("tasks text, date date, description text)")
    cursor.close()

 def select(self: "model") -> tuple:
  """
  Gets all entries from the data base
  :return: Tuple containing all rows of database
  """
  