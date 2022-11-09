# model_backend = 'pylist'
# model_backend = 'sqlite3'
model_backend = 'datastore'

if model_backend == 'sqlite3':
  from .model_sqlite import model
elif model_backend == 'datastore':
  from .model_datastore import model
elif model_backend == 'pylist':
  from .model_pylist import model
else:
  raise ValueError('model_backend not supported')


appmodel = model()

def get_model() -> model:
  return appmodel
