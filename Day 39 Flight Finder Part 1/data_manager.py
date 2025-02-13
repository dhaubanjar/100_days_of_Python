import requests
import os
from dotenv import load_dotenv
load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    SHEETY_ENDPOINT = "https://api.sheety.co/15561209459c28cc04375d00e688f1c1/myFlightDeals/sheet1/"
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")

    def __init__(self):
        self.prices = self.get_prices()

    def get_prices(self):
        response = requests.get(self.SHEETY_ENDPOINT)
        response.raise_for_status()
        prices = response.json()
        return prices

    def update_prices(self, row_id, iata_code):
        UPDATE_ENDPOINT = f"{self.SHEETY_ENDPOINT}{row_id}"
        sheety_parameters = {
            "sheet1" :{
                "iataCode" : iata_code,
            }
        }
        bearer_headers = {
            "Authorization": f"Bearer {self.BEARER_TOKEN}"
        }

        response = requests.put(UPDATE_ENDPOINT, json=sheety_parameters, headers=bearer_headers)
        response.raise_for_status()
