from operator import ge
from wsgiref import headers
import requests
from getpass import getpass

auth_endpoint="http://127.0.0.1:8000/api/auth/"
username=input("Enter your username: ")
password=getpass("Enter your password: ")
auth_response = requests.post(auth_endpoint,json={"username": username, "password":password}) 
print((auth_response).json())

endpoint="http://127.0.0.1:8000/api/profile/"

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    get_response = requests.get(endpoint, headers=headers) 
    print((get_response).json())