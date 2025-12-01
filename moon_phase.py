import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv("./env/.env")
NASA_API_KEY = os.getenv('NASA_KEY')

def nasa_api_request():
    current_time = str(datetime.now(timezone.utc))
    link = f"https://svs.gsfc.nasa.gov/api/dialamoon/{current_time}"
    return link

def main():
    print(nasa_api_request())

if __name__ == "__main__":
    main()
