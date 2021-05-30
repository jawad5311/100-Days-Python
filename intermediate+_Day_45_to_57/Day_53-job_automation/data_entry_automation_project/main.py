
import requests
import bs4
from selenium import webdriver

import os
import dotenv

dotenv.load_dotenv()


response_zillow = requests.get(
    url='https://www.trulia.com/for_rent/San_Francisco,CA/0-1200_price/'
)

# print(response_zillow.text)

print(response_zillow.status_code)

soup = bs4.BeautifulSoup(response_zillow.text, 'html.parser')
# print(soup.prettify())

rent_prices = soup.find_all(attrs={"data-testid": "property-price"})
property_address = soup.find_all(attrs={"data-testid": "property-street"})
property_links = soup.find_all(attrs={"data-testid": "property-price"})
# print(len(prices))

# for price in prices:
#     print(price.text)

