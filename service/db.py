import json

from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb://localhost:27017'
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.service_db


def init_db():
    with open('../db_data.json') as f:
        data = json.load(f)
        db.forms.insert_many(data)
