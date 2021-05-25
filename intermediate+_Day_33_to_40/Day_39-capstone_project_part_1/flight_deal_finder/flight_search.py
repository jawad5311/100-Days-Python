
import os
from pprint import pprint
import datetime as dt
import requests

from flight_data import FlightData

import dotenv
dotenv.load_dotenv()

kiwi_api = os.environ.get('KIWI_API')
kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
kiwi_header = {
    'apikey': kiwi_api
}


current_time = dt.datetime.now()
from_date = (current_time + dt.timedelta(days=3)).strftime('%d/%m/%Y')
to_date = (current_time + dt.timedelta(days=180)).strftime('%d/%m/%Y')


class FlightSearch():
    # def __init__(self):
    #     # self.price = int(price)
    #     # self.air_code = departure_airport_code
    #     # self.depar_city = departure_city
    #     pass

    def get_destination_code(city_name):
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
        #print(response.text)

        code_data = response.json()['locations'][0]['code']
        # pprint(code_data)
        return code_data

    def search_fare_price(self, origin_code, destination_city_code, from_date, to_date):
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
        # print(response.status_code)
        # print(response.json())

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        # print(data)

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
        return flight_data



