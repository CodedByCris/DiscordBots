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