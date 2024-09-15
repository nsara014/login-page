import uuid
from passlib.hash import pbkdf2_sha256
from bson.objectid import ObjectId
from user.db import get_db

db = get_db()

class User:
    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id or uuid.uuid4().hex  # Generate UUID if not provided
        self.name = name
        self.email = email
        self.password = self.encrypt_password(password) if password else None

    @staticmethod
    def encrypt_password(password):
        """Encrypts the password using pbkdf2_sha256."""
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_password(hashed_password, password):
        """Verifies the password."""
        return pbkdf2_sha256.verify(password, hashed_password)

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def get_by_id(user_id):
        """Retrieve a user by ID."""
        user = db.user_db.find_one({"_id": ObjectId(user_id)})
        if user:
            return User(str(user["_id"]), user["name"], user["email"], user["password"])
        return None

    @staticmethod
    def get_all_paginated(page, limit):
        """Retrieve all users with pagination."""
        users = db.user_db.find().skip((page - 1) * limit).limit(limit)
        total = db.user_db.count_documents({})
        return [User(str(user["_id"]), user["name"], user["email"], user["password"]) for user in users], total

    @staticmethod
    def create_user(data):
        """Create a new user."""
        new_user = User(name=data.get("name"), email=data.get("email"), password=data.get("password"))
        result=db.user_db.insert_one(new_user.to_dict())
        return result

    @staticmethod
    def update_user(user_id, data):
        """Update an existing user."""
        user = db.user_db.find_one({"_id": ObjectId(user_id)})
        if not user:
            return None
        
        updated_user = User(user_id, data.get("name"), data.get("email"), password=data.get("password"))
        db.user_db.update_one({"_id": ObjectId(user_id)}, {"$set": updated_user.to_dict()})
        return updated_user

    @staticmethod
    def delete_user(user_id):
        """Delete a user by ID."""
        result = db.user_db.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
