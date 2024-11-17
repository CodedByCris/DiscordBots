# fortnite_api.py
import requests
import os

TOKEN = os.getenv('FORTNITE_TOKEN')

def get_fortnite_stats(player_id):
    url = f"https://api.fortnite.com/stats/{player_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
