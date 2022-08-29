import requests

endpoint="http://127.0.0.1:8000/api/profile/3/update"

data={"first_name":"Jane"}
get_response = requests.get(endpoint, json=data) 
print((get_response).json())