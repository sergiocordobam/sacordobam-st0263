import json
import os
import random
import sys
from threading import Thread
import time

from dotenv import load_dotenv
from flask import Flask, Response, jsonify, request

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
load_dotenv(dotenv_path=env_path)

SERVER_URL = os.getenv("SERVER_URL")
SERVER_PORT = os.getenv("SERVER_PORT")

app = Flask(__name__)

users = {
    "user": "password",
    "admin": "password"
}

files = {}

@app.route("/", methods=["GET"])
def index():
    return "Welcomem, the server is running!"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username] == password:
        return Response(status=200)
    else:
        return Response(status=401)
    
@app.route("/logout", methods=["POST"])
def logout():
    data = request.get_json()
    username = data.get("username")
    if username in users:
        return Response(status=200)
    else:
        return Response(status=401)
    
@app.route("/upload_file", methods=["POST"])
def upload_file():
    data = request.get_json()
    url = data.get("url")
    if not url:
        return Response(status=400)
    else:
        return jsonify(url=url, status=200)
    
@app.route("/download_file", methods=["POST"])
def download_file():
    data = request.get_json()
    file_name = data.get("file_name")
    if file_name in files:
        url = files[file_name]
        return jsonify(url=url, status=200)
    else:
        return Response(status=404)
    
if __name__ == "__main__":
    app.run(host=SERVER_URL, port=SERVER_PORT)
