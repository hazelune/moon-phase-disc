import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone, timedelta
import json

load_dotenv("./env/.env")
NASA_API_KEY = os.getenv('NASA_KEY')

# nasa's api returns phase as percentage of illumination. this makes it emoji!
def illumination_to_phase(current, previous):
    # handling this first, since if current = previous, then it's surrounding a new or full
    if current < 1:
        return "🌑"
    if current > 99:
        return "🌕"
    # assume waxing, if current illumination is less than previous, then obviously waning
    waxing = None
    if current < previous:
        waxing = False
    else:
        waxing = True
    
    # and a bunch of case matchin
    if waxing == True:
        if current < 50:
            return "🌒"
        elif current > 51: 
            return "🌔"
        else:
            return "🌓"
    else:
        if current < 50:
            return "🌘"
        elif current > 51:
            return "🌖"
        else:
            return "🌗"


# sometimes the nasa api doesn't have a functional response for all recent times
# this function finds the most recent functional one to go off of
def most_recent_nasa_resp(starting_dt = datetime.now(timezone.utc)):
    # take input and make response
    current_datetime = starting_dt
    current_dt_str = current_datetime.strftime("%Y-%m-%dT%H:%M")
    current_link = f"https://svs.gsfc.nasa.gov/api/dialamoon/{current_dt_str}"
    current_response = requests.get(url = current_link)

    # test if response works, if not, go a minute back and retry
    while True:
        try:
            current_response.json()
            break
        except json.JSONDecodeError:
            current_datetime = current_datetime - timedelta(minutes = 1)
            current_dt_str = current_datetime.strftime("%Y-%m-%dT%H:%M")
            current_link = f"https://svs.gsfc.nasa.gov/api/dialamoon/{current_dt_str}"
            current_response = requests.get(url = current_link)
            print(f'Request failed, rewinding to {current_dt_str} and trying again.')
    return current_response

# does the legwork of grabbing everything 
def nasa_api_request():
    # fetching current time and previous time for comparison (for waxing/waning)
    current_response = most_recent_nasa_resp()
    previous_response = most_recent_nasa_resp(datetime.now(timezone.utc) - timedelta(hours = 1))
    if current_response.status_code != 200 and previous_response.status_code != 200:
        print(f"Error: {current_response.status_code}")
    else:
        # fetching illumination and converting to phase
        current_illumination = current_response.json()["phase"]
        previous_illumination = previous_response.json()["phase"]
        phase = illumination_to_phase(current_illumination, previous_illumination)
        return(phase)

def main():
    print(nasa_api_request())

if __name__ == "__main__":
    main()
