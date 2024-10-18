#!/usr/bin/python3
"""
Flask API to manage a list of users. This API supports adding users, retrieving a list 
of usernames, fetching user details, and checking the API status. It uses JSON for 
communication and handles basic CRUD operations for user management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """
    home - Display the home route message

    Return:
    A welcome message string for the home route
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    get_data - Return a list of all usernames

    Return:
    A JSON list of all usernames in the 'users' dictionary
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    status - Return the status of the API

    Return:
    A string "OK" to indicate the API is running correctly
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    get_user - Retrieve user details by username

    @arg: username - The username for which to fetch details

    Return:
    JSON user details if found, otherwise an error message with status code 404
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add_user - Add a new user to the API

    Return:
    JSON message indicating success, and the added user details.
    If username is not provided, return an error with status code 400
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
# main - Start the Flask development server
    app.run()
