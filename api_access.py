import requests
from oauthlib.oauth2 import WebApplicationClient

CLIENT_ID = "1444796196999794881"
CLIENT_SECRET = "OxP_eIMwXdWUaDvALlObM3gJXSjAkntU"
REDIRECT_URI = "http://localhost:8080"

client = WebApplicationClient(CLIENT_ID)
DISCORD_AUTHORIZATION_URL = "https://discord.com/oauth2/authorize"

SCOPES = ["identify"]
url = "https://discord.com/api/v10"

def auth():
    request_url = client.prepare_request_uri(
            DISCORD_AUTHORIZATION_URL,
            redirect_uri = REDIRECT_URI,
            # implement state later for security if made public?
            scope = SCOPES
    )
    print(f"Authenticate at {request_url}")


def api_output(str = ""):
    response = requests.get(url)
    return response

def main():
    auth()
    

if __name__ == "__main__":
    main()




