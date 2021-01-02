import os

import hug
from mongoengine import connect

if not (MONGO_HOST := os.getenv('MONGO_HOST')):
    raise RuntimeError('Missing `MONGO_HOST` environment variable..')

connect(host=MONGO_HOST)


@hug.get()
def health():
    return {'status': 'ok'}
