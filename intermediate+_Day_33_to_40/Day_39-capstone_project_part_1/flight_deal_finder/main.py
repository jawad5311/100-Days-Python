
import os
import requests
from pprint import pprint

import flight_search
import data_manager

import dotenv
dotenv.load_dotenv()


sheety_api = os.environ.get('SHEETY_API')
kiwi_api = os.environ.get('KIWI_API')
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')


data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()

sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

data_manager.update_destination_code()
pprint(sheet_data)


