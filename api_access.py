import requests
import os
import json
from dotenv import load_dotenv

from moon_phase import nasa_api_request

load_dotenv("./env/.env")
TOKEN = os.getenv('TOKEN')
USER_URL = "https://discord.com/api/v10/users/@me/settings"

def change_status(emoji, text = None):
    headers = {
            'Authorization': TOKEN,
            'Content-Type': 'application/json'
    }
    payload = {
            "custom_status": {
                "text": text,
                "emoji_name": emoji
            }
    }
    response = requests.patch(
            url = USER_URL,
            headers = headers,
            json = payload
    )
    response.raise_for_status()

def main():
    current_phase = nasa_api_request()
    change_status(current_phase)

if __name__ == "__main__":
    main()




