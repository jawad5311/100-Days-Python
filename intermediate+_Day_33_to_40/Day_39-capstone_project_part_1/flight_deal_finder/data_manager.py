
import requests
import os

from flight_search import FlightSearch

import dotenv
dotenv.load_dotenv()

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')
sheety_api = os.environ.get('SHEETY_API')


sheety_header = {
    'Authorization': f'Bearer {sheety_api}'
}


class DataManager(FlightSearch):
    def __init__(self):
        self.destination_data = [
          {'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
          {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
          {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
          {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
          {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
          {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
          {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
          {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
          {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]


    # def get_destination_data(self):
    #     response = requests.get(sheety_endpoint)
    #     data = response.json()['sheet1']
    #     self.destination_data = data
    #     return self.destination_data

    def update_destination_code(self):
        print(self.destination_data)
        for row in self.destination_data:
            city = row['city']
            print(city)
            print(type(city))
            iataCode = row['iataCode']
            if iataCode == '':
                new_data = {
                    'sheet1': {
                        'iataCode': FlightSearch.get_destination_code(city)
                    }
                }
                response = requests.put(
                    url=f"{sheety_endpoint}/{row['id']}",
                    headers= sheety_header,
                    json = new_data
                )
                print(response.status_code)
                print(response.text)

        print(self.destination_data)


# def destination_code():
#     # city = "TESTING"
#     return "testing"

# def update_destination_code():
#     print(destination_data)
#     for row in destination_data:
#         city = row['city']
#         print(city)
#         print(type(city))
#         iataCode = row['iataCode']
#         if iataCode == '':
#             row['iataCode'] = destination_code()
#
#     print(destination_data)


# update_destination_code()