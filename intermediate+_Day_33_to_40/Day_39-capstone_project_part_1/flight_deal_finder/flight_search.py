
# Required modules
import os
import datetime as dt
import requests

# Project Files
from flight_data import FlightData

import dotenv
dotenv.load_dotenv()  # Loads .env file

# KIWI endpoints, api, & header
kiwi_api = os.environ.get('KIWI_API')
kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
kiwi_header = {
    'apikey': kiwi_api
}


class FlightSearch():
    """ Search flights for required destinations """
    def get_destination_code(city_name):
        """ Return iataCode of the city """
        kiwi_parameters = {
            'term': city_name,
            "location_types": "city"
        }
        response = requests.get(
            url= kiwi_endpoint,
            headers= kiwi_header,
            params= kiwi_parameters
        )
        print(response.status_code)

        code_data = response.json()['locations'][0]['code']
        return code_data

    def search_fare_price(self, origin_code, destination_city_code, from_date, to_date):
        # Parameters use to get the flights data
        kiwi_parameters = {
            "fly_from": origin_code,
            "fly_to": destination_city_code,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(
            url=kiwi_endpoint,
            headers= kiwi_header,
            params= kiwi_parameters
        )
        # Handles the IndexError exception
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        else:
            # Create flight object of the data returned from the kiwi response
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data  # Return the flight data object



