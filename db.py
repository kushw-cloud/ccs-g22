from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cyber_incidents"]
collection = db["real_time_data"]

def insert_incident(incident):
    collection.insert_one(incident)

def get_incidents():
    return list(collection.find({}, {"_id": 0}))
