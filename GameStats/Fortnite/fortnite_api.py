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

def get_today_shop():
    url = "https://fortnite-api.com/v2/shop"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        items = data.get("data", {}).get("featured", {}).get("entries", [])
        shop_message = "Today's Fortnite Shop:\n"
        for item in items:
            item_name = item.get("items", [{}])[0].get("name", "Unknown")
            shop_message += f"- {item_name}\n"
        return shop_message
    else:
        return "Failed to retrieve the shop data."