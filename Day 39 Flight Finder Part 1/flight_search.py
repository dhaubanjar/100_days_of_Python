import os
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv('FLIGHTS_API_KEY')
        self._api_secret = os.getenv('FLIGHTS_API_SECRET')
        self._token = self._get_new_token()
    def get_iata_code(self, city_name):
        return "TESTING1"

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        body = {
            'grant_type' : 'client_credentials',
            'client_id' : self._api_key,
            'client_secret' : self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        response.raise_for_status()
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']