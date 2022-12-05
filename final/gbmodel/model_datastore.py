from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """
    Translates Datastore results into the format expected by the application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}, ...]

    This returns:
        [ img, text_prompt, date ]

    where img is a image files,
    text_prompt is a string, and date is a datetime object.
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()

    return [entity['img'], entity['text_prompt'], entity['date']]

class model(Model):
  def __init__(self):
    self.client = datastore.Client('flask-ai-py-app')

  def select(self):
    query = self.client.query(kind= 'Text2Image')
    entities = list(map(from_datastore, query.fetch()))
    return entities

  def insert(self, img, text_prompt):
    key = self.client.key('Text2Image')
    text_image = datastore.Entity(key)
    text_image.update({
      'img': img,
      'text_prompt': text_prompt,
      'date': datetime.now()
    })
    self.client.put(text_image)
    return True
