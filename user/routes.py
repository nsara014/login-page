from flask import Blueprint, jsonify, request, abort
from user.models import User

user_bp = Blueprint('user', __name__)

# GET /users - Returns a paginated list of all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        
        users, total = User.get_all_paginated(page, limit)
        return jsonify({
            "users": [user.to_dict() for user in users],
            "total": total,
            "page": page,
            "limit": limit
        }), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# GET /users/<id> - Returns the user with the specified ID
@user_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.get_by_id(id)
    if user:
        return jsonify(user.to_dict()), 201
    else:
        return abort(404, description="User not found")

# POST /users - Creates a new user
@user_bp.route('/users', methods=['POST'])
def post_user():
    data = request.get_json()
    
    result = User.create_user(data)
    return jsonify({"id": str(result.inserted_id), "message": "User created"}), 202

# PUT /users/<id> - Updates the user with the specified ID
@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    
    updated_user = User.update_user(id, data)
    if updated_user:
        return jsonify({"message": "User updated"}), 203
    else:
        return abort(404, description="User not found")

# DELETE /users/<id> - Deletes the user with the specified ID
@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    success = User.delete_user(id)
    if success:
        return jsonify({"message": "User deleted"}), 200
    else:
        return abort(404, description="User not found")
