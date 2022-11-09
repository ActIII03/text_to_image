from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
  """
  Transforms a Datastore entity into a format suitable for the
  application

  :param entity: Datastore entity
  :return: Dictionary containing the entity properties
  """
  if not entity:
      return None
  if isinstance(entity, list):
    entity = entity.pop()
  return [entity['task'], entity['date'], entity['due_date'], entity['description']]

class model(Model):
  def __init__(self):
    self.client = datastore.Client('hw4-todo-368106')

  def select(self):
    """
    Gets all entries from the database
    :return: list containing all rows of database
    """
    query = self.client.query(kind='Task')
    entities = list(map(from_datastore, query.fetch()))
    return entities
  
  def insert(self, task: "str", date: "date", due_date: "date", description: "str"):
    """
    Inserts a new entry into the database
    :param task: Task name
    :param date: Date of task creation
    :param due_date: Date of task due
    :param description: Description of task
    :return: None
    """
    key = self.client.key('Task')
    task = datastore.Entity(key)
    task.update({
      'task': task,
      'date': date,
      'due_date': due_date,
      'description': description
    })
    self.client.put(task)
    return True
