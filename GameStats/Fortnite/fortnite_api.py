# fortnite_api.py
import requests

TOKEN = None

def set_fortnite_token(token):
    global TOKEN
    TOKEN = token

def get_fortnite_stats():
    url = "https://fortniteapi.io/v2/lookup"
    headers = {
        'Authorization': TOKEN
    }
    params = {
        'username': "AsianCriss7777",
        'platform': "epic",
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}")
        return None
