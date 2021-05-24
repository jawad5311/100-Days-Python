

import os
import requests
import pprint

import dotenv
dotenv.load_dotenv()


sheety_api = os.environ.get('SHEETY_API')
kiwi_api = os.environ.get('KIWI_API')

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

response = requests.get(sheety_endpoint)
sheet_data = response.json()['sheet1']

pprint.pprint(sheet_data)




