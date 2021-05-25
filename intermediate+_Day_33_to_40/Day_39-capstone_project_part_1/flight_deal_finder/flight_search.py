
import os
from pprint import pprint

import dotenv
import requests


dotenv.load_dotenv()

kiwi_api = os.environ.get('KIWI_API')
kiwi_endpoint = "https://tequila-api.kiwi.com/locations/query"
kiwi_header = {
    'apikey': kiwi_api
}


class FlightSearch:

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
        pprint(code_data)
        return code_data


# fs = FlightSearch()
#
# fs.get_destination_code('paris')