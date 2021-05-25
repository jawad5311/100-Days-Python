
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
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            sheety_endpoint,
            headers= sheety_header
        ).json()
        self.destination_data = response['sheet1']
        # self.update_destination_code()
        return self.destination_data

    def update_destination_code(self):
        for row in self.destination_data:
            # print(city)
            iata_code = row['iataCode']
            # print(row)
            if iata_code == '':
                city = row['city']
                new_data = {
                    'sheet1': {
                        'iataCode': FlightSearch.get_destination_code(city_name=city)
                    }
                }
                response = requests.put(
                    url=f"{sheety_endpoint}/{row['id']}",
                    headers= sheety_header,
                    json = new_data
                )
                print(response.status_code)
                print(response.text)

        self.get_destination_data()