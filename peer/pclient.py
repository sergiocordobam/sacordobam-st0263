import os
import sys
from threading import Thread

import dotenv
import grpc
import pserver_pb2
import pserver_pb2_grpc
from pserver import pserver

env_path = os.path.join(os.path.dirname(__file__), sys.argv[1])
dotenv.load_dotenv(dotenv_path=env_path)

PSERVER_PORT = os.getenv("PSERVER_PORT")
PSERVER_URL = os.getenv("PSERVER_URL")

def login(stub):
    username = input("Enter username: ")
    password = input("Enter password: ")
    response = stub.Login(pserver_pb2.UserData(username=username, password=password))
    if response.status == 401:
        print("Invalid username or password!")
        username = input("Enter username: ")
        password = input("Enter password: ")
        response = stub.Login(pserver_pb2.UserData(username=username, password=password))
    elif response.status == 200:
        print("Login successful!")
    return username

if __name__ == "__main__":
    pserver_channel = grpc.insecure_channel(f"{PSERVER_URL}:{PSERVER_PORT}")
    pserver_stub = pserver_pb2_grpc.PServerStub(pserver_channel)
    username = login(pserver_stub)
    print("Username:", username)
    pserver_thread = Thread(target=pserver.serve)
    pserver_thread.start()
    while True:
        print("Choose an option:")
        print("1. Upload file")
        print("2. Download file")
        print("3. Logout")
        option = input("Enter option: ")
        if option == "1":
            file_name = input("Enter file name: ")
            request = pserver_pb2.File(file_name=file_name, username=username)
            info = pserver_stub.UploadFile(request)
            if info.status == 200:
                print("File uploaded successfully!")
            else:
                print("File upload failed!")
        elif option == "2":
            file_name = input("Enter file name: ")
            request = pserver_pb2.File(file_name=file_name, username=username)
            info = pserver_stub.DownloadFile(request)
            if info.status == 200:
                print("File downloaded successfully!")
            else:
                print("File download failed!")
        elif option == "3":
            response = pserver_stub.Logout(pserver_pb2.Username(username=username))
            if response.status == 200:
                print("Logout successful!")
                break
            else:
                print("Logout failed!")
        break