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
  connection = sqlite3.connect(DB_FILE)
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM tasks")
  return cursor.fetchall()

# return true
def insert(self: "model", task: str, date: date, description: str) -> bool:
  """
  Inserts a new entry into the database
  :param task: Task name
  :param date: Date of task
  :param description: Description of task
  :return: None
  """
  params = {'task': task, 'date': date.today(), 'description': description}
  connection = sqlite3.connect(DB_FILE)
  cursor = connection.cursor()
  cursor.execute("INSERT INTO tasks VALUES(:task, :date, :description)", params)

  connection.commit()
  cursor.close()
  return True
  