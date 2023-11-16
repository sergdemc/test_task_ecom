import json
import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb://localhost:27017'
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.service_db


def init_db():
    json_file = os.path.join(os.path.dirname(__file__), '..', 'db_data.json')
    with open(json_file) as f:
        data = json.load(f)
        db.forms.insert_many(data)
