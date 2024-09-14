# db.py
import pymongo

def get_db():
    # Use the Docker Compose service name 'db' as the host
    client = pymongo.MongoClient('mongodb://root:pass@db:27017/?authSource=admin')
    db = client.user_db
    return db
