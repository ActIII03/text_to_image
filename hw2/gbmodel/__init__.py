# model backend is sqlite3
model_backend = 'sqlite3'

if model_backend == 'sqlite3':
  from .model_sqlite3 import model
elif model_backend == 'pylist':
  from .model_pylist import model
else:
  raise ValueError('model_backend not supported')


appmodel = model()

def get_model() -> model:
  return appmodel
