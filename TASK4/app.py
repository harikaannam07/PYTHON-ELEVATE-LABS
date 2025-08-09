from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST - Add new user
@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.get_json()
    new_user["id"] = users[-1]["id"] + 1 if users else 1
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    updated_data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(updated_data)
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# DELETE - Remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
