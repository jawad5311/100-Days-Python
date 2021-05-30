
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
property_address_1 = soup.find_all(attrs={"data-testid": "property-street"})
property_address_2 = soup.find_all(attrs={"data-testid": "property-region"})
links = soup.find_all(name='a', attrs={"data-testid": "property-card-link"})

property_rents = [rent.text for rent in rent_prices]
property_addr_1 = [adr.text for adr in property_address_1]
property_addr_2 = [adr.text for adr in property_address_2]
property_links = [link['href'] for link in links]

print(len(property_rents))
print(property_rents)
print(len(property_addr_1))
print(property_addr_1)
print(len(property_addr_2))
print(property_addr_2)
print(len(property_links))
print(property_links)



