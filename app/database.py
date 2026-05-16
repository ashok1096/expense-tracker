import os
from pymongo import MongoClient

# MONGODB ATLAS CONNECTION
MONGO_URL = os.getenv("MONGO_URL", "mongodb://127.0.0.1:27017")

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

# DATABASE
db = client["expense_tracker"]

# COLLECTIONS
category_collection = db["categories"]

expenses_collection = db["expenses"]