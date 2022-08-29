import requests

endpoint="http://127.0.0.1:8000/api/profile/"

data = {'first_name': 'John', 
'last_name': 'Doe', 
'birth_date': '1999-01-12', 
'address1': '123 abc ave', 
'address2': '123', 
'city': 'Dallas', 
'county': 'Dallas', 
'state': 'Texas', 
'zipcode': '00000', 
'phone': 4765456789,
}
get_response = requests.post(endpoint, json=data) 
print((get_response).json())