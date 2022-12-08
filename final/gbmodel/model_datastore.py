from .Model import Model
from datetime import datetime
import os
from io import BytesIO

from google.cloud import datastore
from google.cloud import storage


def from_datastore(entity):
    """
    Translates Datastore results into the format expected by the application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}, ...]

    This returns:
        [ img, text_prompt, date ]

    where img is an image url,
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
    self.image_bucket = storage.Client().get_bucket('final-python-textimage')

  def select(self):
    query = self.client.query(kind= 'Text2Image')
    entities = list(map(from_datastore, query.fetch()))
    return entities

  def insert(self, img, text_prompt):
    """
    Inserts a new Text2Image into Datastore and also uploads the image to Cloud Storage.
    :param img: image file
    :param text_prompt: string
    :return: True if Text2Image created, otherwise False
    """
    key = self.client.key('Text2Image')
    text_image = datastore.Entity(key)
    # Upload image to Cloud Storage and get public URL for Text2Image entity
    blob = self.image_bucket.blob(datetime.now().isoformat() + '.png')
    myImage = BytesIO(img)
    blob.upload_from_file(myImage, content_type='image/png')
    blob.make_public()

    text_image.update({
      'img': blob.public_url,
      'text_prompt': text_prompt,
      'date': datetime.now()
    })
    self.client.put(text_image)
    return True
