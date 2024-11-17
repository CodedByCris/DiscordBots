# valorant_api.py
import requests
import os

TOKEN = os.getenv('VALORANT_TOKEN')
def get_valorant_stats(player_id):
    url = f"https://api.valorant.com/stats/{player_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None