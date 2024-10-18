#!/usr/bin/env python3
"""
This Flask-based API implements both HTTP Basic Authentication and JWT (JSON Web Token)
authentication mechanisms. The API supports user login, basic auth-protected endpoints,
and role-based access for admin users using JWT tokens. The application handles various
error cases like unauthorized access, invalid or expired tokens, and revoked tokens.
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    """
    verify_password - Verifies the password for HTTP Basic Authentication

    @arg: username - The username to check
    @arg: password - The password to validate

    Return:
    The user object if credentials are valid, otherwise None
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    basic_protected - An endpoint protected by HTTP Basic Authentication

    Return:
    A message granting access to the basic-protected route
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    login - Handles user login, validates credentials, and generates a JWT token

    Return:
    A JWT access token if credentials are valid, otherwise an error message
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username,
                                                     'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    jwt_protected - An endpoint protected by JWT authentication

    Return:
    A message granting access to the JWT-protected route
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    admin_only - An endpoint accessible only to users with the 'admin' role

    Return:
    A message granting access if the user is an admin, otherwise an error
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    handle_unauthorized_error - Handles requests missing or with invalid JWT tokens

    Return:
    An error message indicating unauthorized access
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    handle_invalid_token_error - Handles requests with invalid JWT tokens

    Return:
    An error message indicating an invalid token
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    handle_expired_token_error - Handles requests with expired JWT tokens

    Return:
    An error message indicating that the token has expired
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    handle_revoked_token_error - Handles requests with revoked JWT tokens

    Return:
    An error message indicating that the token has been revoked
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    handle_needs_fresh_token_error - Handles requests requiring a fresh JWT token

    Return:
    An error message indicating that a fresh token is required
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
