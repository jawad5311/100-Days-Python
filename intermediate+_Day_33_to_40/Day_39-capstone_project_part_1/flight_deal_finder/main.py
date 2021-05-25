
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


data_manager = data_manager.DataManager().update_destination_code()
flight_search = flight_search.FlightSearch()

# data = data_manager.get_destination_data()
# # pprint(data)
#
# data = data_manager.update_destination_code()


# response = requests.get(sheety_endpoint)
# sheet_data = response.json()  #['sheet1']

#
# sheet_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#               {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#               {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
#               {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
#               {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
#               {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
#               {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
#               {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
#               {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]

# for data in sheet_data:
#     city_code = data['iataCode']
#     # print(city_code == '')
#     if city_code == '':
#         data['iataCode'] = flight_search.destination_code(data['city'])
#
# pprint(sheet_data)

# pprint.pprint(sheet_data)

# iata = flight_search.FlightSearch()
#
#
# sheet_data = data_manager.get_destination_data()


# print(sheet_data)

# code = iata.IATAcode()
#
# print(code)

# for item in sheet_data:
#     item = item['iataCode']
#     print(item is None)
#
# print(item['city'])
