import os
import sys
import time
from concurrent import futures

import dotenv
import grpc
import pserver_pb2
import pserver_pb2_grpc
import requests
from flask import Flask
from threading import Thread

app = Flask(__name__)

env_path = os.path.join(os.path.dirname(__file__), sys.argv[2])
dotenv.load_dotenv(dotenv_path=env_path)

SERVER_URL = os.getenv("SERVER_URL")
SERVER_PORT = os.getenv("SERVER_PORT")

PSERVER_PORT = os.getenv("PSERVER_PORT")
PSERVER_URL = os.getenv("PSERVER_URL")

files = []

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(f"{PSERVER_URL}:{PSERVER_PORT}")
    pserver_pb2_grpc.add_PServerServicer_to_server(PServerServicer(), server)
    server.start()
    server.wait_for_termination()

def login(pclient_data):
    username = pclient_data.get("username")
    password = pclient_data.get("password")
    url = f"{SERVER_URL}:{SERVER_PORT}"
    pserver_data = {
        "username": username,
        "password": password,
    }
    response = requests.post(f"http//{PSERVER_URL}:{PSERVER_PORT}/login", json=pserver_data)
    return response

def upload_file(file_name):
    url = f"{SERVER_URL}:{SERVER_PORT}"
    pserver_data = {
        "file_name": file_name,
        "url": url
    }
    response = requests.post(f"http//{PSERVER_URL}:{PSERVER_PORT}/upload_file", json=pserver_data)
    return response

def download_file(file_name):
    url = f"{SERVER_URL}:{SERVER_PORT}"
    pserver_data = {
        "file_name": file_name,
    }
    response = requests.post(f"http//{PSERVER_URL}:{PSERVER_PORT}/download_file", json=pserver_data)
    return response

def ping():
    global ping_status
    while ping_status:
        response = requests.get(f"http//{PSERVER_URL}:{PSERVER_PORT}/ping", json={"url": f"{SERVER_URL}:{SERVER_PORT}"})
        time.sleep(5)

def send_index():
    pserver_data = {
        "files": files,
        "url": f"{SERVER_URL}:{SERVER_PORT}"
    }
    response = requests.post(f"http//{PSERVER_URL}:{PSERVER_PORT}/index", json=pserver_data)
    return response

class PServerServicer(pserver_pb2_grpc.PServerServicer):
    def Login(self, request, context):
        username = request.username
        password = request.password
        response = login({"username": username, "password": password})
        return pserver_pb2.Response(status_code=response.status_code)


    def Logout(self, request, context):
        username = request.username
        response = requests.post(f"http//{PSERVER_URL}:{PSERVER_PORT}/logout", json={"username": username})
        return pserver_pb2.Response(status_code=response.status_code)

    def DownloadFileRequest(self, request, file_name, context):
        url = f"{SERVER_URL}:{SERVER_PORT}"
        pserver_data = {
            "file_name": file_name,
            "url": url
        }
        response = requests.post(f"http//{PSERVER_URL}:{PSERVER_PORT}/download_file", json=pserver_data)
        return pserver_pb2.Response(status_code=response.status_code)

    def DownloadFile(self, request, context):
        file_name = request.file_name
        response = download_file(file_name)
        return pserver_pb2.Response(status_code=response.status_code)

    def UploadFileRequest(self, request, context):
        file_name = request.file_name
        response = upload_file(file_name)
        return pserver_pb2.Response(status_code=response.status_code)

    def UploadFile(self, request, context):
        file_name = request.file_name
        response = upload_file(file_name)
        return pserver_pb2.Response(status_code=response.status_code)
    
if __name__ == "__main__":
    serve()
