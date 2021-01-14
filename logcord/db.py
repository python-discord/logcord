import os

from pymongo import MongoClient

if not (MONGO_HOST := os.getenv('MONGO_HOST')):
    raise RuntimeError('Missing `MONGO_HOST` environment variable..')

client = MongoClient(MONGO_HOST)
db = client.get_default_database()
