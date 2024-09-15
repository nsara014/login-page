# db.py
import pymongo

def get_db():
    # Use the Docker Compose service name 'db' as the host
    client = pymongo.MongoClient('mongodb://root:pass@db:27017/?authSource=admin',maxPoolSize=50,  
        minPoolSize=1,  
        maxIdleTimeMS=300000 )
    db = client.user_db
    db.user_db.create_index([("id", pymongo.ASCENDING)], unique=True)
    db.user_db.create_index([("name", pymongo.ASCENDING)])

    return db
