
import os
import requests
from pprint import pprint
from datetime import datetime, timedelta

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

ORIGIN_CITY_IATA = "LON"

current_time = datetime.now()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
from_date = (current_time + timedelta(days=3)).strftime('%d/%m/%Y')
to_date = (current_time + timedelta(days=180)).strftime('%d/%m/%Y')

for destination in sheet_data:
    flight = flight_search.search_fare_price(
        origin_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_date=from_date,
        to_date=to_date
    )


