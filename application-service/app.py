from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

USER_SERVICE_URL = 'http://user-service:5001'

@app.route('/users', methods=['GET'])
def get_all_users():
    response = requests.get(f"{USER_SERVICE_URL}/users")
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Unable to fetch users from user service"}), 500
    
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    response = requests.post(f"{USER_SERVICE_URL}/users", json=user_data)
    return jsonify(response.json()), response.status_code

# Get user via user-service
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    return jsonify(response.json()), response.status_code

# Update user via user-service
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    response = requests.put(f"{USER_SERVICE_URL}/users/{user_id}", json=user_data)
    return jsonify(response.json()), response.status_code

# Delete user via user-service
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = requests.delete(f"{USER_SERVICE_URL}/users/{user_id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Expose Application Service on port 5000
