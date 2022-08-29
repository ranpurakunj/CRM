import requests

profile_id = input("What ID do you want to delete?")
try:
    profile_id=int(profile_id)
except:
    profile_id=None 
    print(f'{profile_id} is not valid id')

if profile_id:
    endpoint=f"http://127.0.0.1:8000/api/profile/{profile_id}/delete"

    get_response = requests.delete(endpoint) 
    print((get_response).status_code, get_response.status_code==204)