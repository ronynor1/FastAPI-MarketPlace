"""
MongoDB Setup
"""
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.getenv("MONGODB_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.marketplace

users_collection = db["users_collection"]
products_collection = db["products_collection"]
orders_collection = db["orders_collection"]
orders_history_collection = db["orders_history_collection"]
roles_permissions = db["roles_permissions"]
