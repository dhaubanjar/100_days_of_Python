import requests


AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, price, origin_airport, departure_airport_code, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.departure_airport_code = departure_airport_code
        self.out_date = out_date
        self.return_date = return_date

    def find_cheapest_flight(self):
        amadeus_parameters = {
            "originLocationCode": "LON",
            "destinationLocationCode": "JFK",
            "departureDate" : "2024-12-28",
            "returnDate" : "2025-01-01",
            "adults" : 1,
            "travelClass" : "ECONOMY",
            "nonStop" : "True",
            "currencyCode" : "GBP",
            "max" : 5,
        }
        response = requests.get(AMADEUS_ENDPOINT, params=amadeus_parameters)
        response.raise_for_status()
        amadeus_flight_prices = response.json()
        print(amadeus_flight_prices)

