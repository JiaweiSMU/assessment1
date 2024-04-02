from flask import Flask, jsonify
from flask_cors import CORS
import logging
import requests


app = Flask(__name__)
CORS(app)


@app.route("/getUsers", methods=["GET"])
def get_users():
    """
    Retrieves a list of users from the API and returns it as a JSON response.

    Returns:
        - If the request is successful, returns a JSON response containing the list of users.
        - If the request fails, returns a JSON response with an error message and a status code of 400.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        users = response.json()
        logging.info(users)
        return jsonify(users)
    else:
        return jsonify(error="Unable to fetch users"), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)