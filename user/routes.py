from flask import Blueprint, jsonify, request, abort
from user.models import User
from user.db import get_db
from bson.objectid import ObjectId

user_bp = Blueprint('user', __name__)
db = get_db()

# GET /users - Returns a list of all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    _users = db.user_db.find()
    users = [User(str(user["_id"]), user["name"], user["email"], user["password"]).to_dict() for user in _users]
    return jsonify({"users": users}), 200

# GET /users/<id> - Returns the user with the specified ID
@user_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = db.user_db.find_one({"_id": ObjectId(id)})
    if user:
        user_obj = User(str(user["_id"]), user["name"], user["email"], user["password"])
        return jsonify(user_obj.to_dict()), 201
    else:
        return abort(404, description="User not found")

# POST /users - Creates a new user with the specified data, UUID generation, and password encryption
@user_bp.route('/users', methods=['POST'])
def post_user():
    data = request.get_json()
    
    # Create a new User object
    new_user = User(name=data.get("name"), email=data.get("email"), password=data.get("password"))
    
    # Insert into the database
    result = db.user_db.insert_one(new_user.to_dict())
    return jsonify({"id": str(result.inserted_id), "message": "User created"}), 202

# PUT /users/<id> - Updates the user with the specified ID, encrypting password if provided
@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.get_json()
        user = db.user_db.find_one({"_id": ObjectId(id)})
        if not user:
            return abort(404, description="User not found")

        # Update user data
        updated_user = User(id, data.get("name"), data.get("email"), password=data.get("password"))
        db.user_db.update_one({"_id": ObjectId(id)}, {"$set": updated_user.to_dict()})
        return jsonify({"message": "User updated"}), 203
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


# DELETE /users/<id> - Deletes the user with the specified ID
@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = db.user_db.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return abort(404, description="User not found")
    return jsonify({"message": "User deleted"}), 200
