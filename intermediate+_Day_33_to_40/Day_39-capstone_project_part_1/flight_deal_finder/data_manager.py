
# Required modules
import requests
import os

# Project Files
from flight_search import FlightSearch

import dotenv
dotenv.load_dotenv()  # Loads .env file


# SHEETY endpoints, api, & header
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')
sheety_api = os.environ.get('SHEETY_API')
sheety_header = {
    'Authorization': f'Bearer {sheety_api}'
}


class DataManager(FlightSearch):
    """ Get data from google sheets and update iataCodes """
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """ Get data from google sheets """
        response = requests.get(
            sheety_endpoint,
            headers= sheety_header
        ).json()
        self.destination_data = response['sheet1']
        # self.update_destination_code()
        return self.destination_data

    def update_destination_code(self):
        """ Update iataCode of the cities """
        for row in self.destination_data:
            iata_code = row['iataCode']
            if iata_code == '':
                city = row['city']
                new_data = {  # Holds data to be used to update google sheets
                    'sheet1': {
                        'iataCode': FlightSearch.get_destination_code(city_name=city)
                    }
                }
                # Send put request to google sheets to update data
                response = requests.put(
                    url=f"{sheety_endpoint}/{row['id']}",
                    headers= sheety_header,
                    json = new_data
                )
                print(response.status_code)  # Provides with the status of the request

        self.get_destination_data()