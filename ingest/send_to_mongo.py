from pymongo import MongoClient
from parse_json import load_json_data

def connect_to_mongo(uri="mongodb://localhost:27017/", db_name="demo", collection_name="people"):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

def insert_data(collection, data):
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

if __name__ == "__main__":
    data = load_json_data('../data/sample_data.json')
    collection = connect_to_mongo()
    insert_data(collection, data)
    print(f"Inserted {len(data)} documents in MongoDB.")
