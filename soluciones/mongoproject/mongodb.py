from pymongo import MongoClient
import os
import config


connectionURL=os.getenv("MONGODB_URL")
client = MongoClient(connectionURL)
print(f"Connected to mongodb in -> {connectionURL}")

def getClient():
    return client

def getCollection(colName, dbName="mibbdd"):   
    db = client[dbName]
    col = db[colName]
    return db, col