#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData

# create an instance of DataManager
# data_manager = DataManager()
search_flight = FlightSearch()              # create an instance of FlightSearch
flight_data = FlightData()

# sheet_data = data_manager.get_prices()      # gets price from Google sheet

""" Checks if IATA Codes column is empty or not """
# pprint(sheet_data)
# for entry in sheet_data['sheet1']:
#     if entry['iataCode'] == '':
#         city_name = entry['city']
#         row_id = entry['id']
#         iata_code = search_flight.get_iata_code(city_name)
#         data_manager.update_prices(row_id, iata_code)
#         entry['iataCode'] = iata_code



search_flight.get_new_token()