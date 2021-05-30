
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
property_href = [link['href'] for link in links]

# print(len(property_rents))
print(property_rents)
# print(len(property_addr_1))
# print(property_addr_1)
# print(len(property_addr_2))
# print(property_addr_2)
# print(len(property_href))
# print(property_href)

# property_rents = ['$900 - $1,045/mo', '$895/mo', '$1,145 - $1,995/mo', 'Contact For Price', '$1,195/mo', '$1,150/mo', '$1,195/mo', '$1,195/mo', '$1,100/mo', '$1,200/mo', '$1,200/mo', '$1,195 - $1,395/mo', '$1,195/mo', '$1,200/mo', '$1,095 - $1,730/mo', '$695/mo', '$1,200/mo', '$1,100/mo']
# property_addr_1 = ['1000-1010 Bush Street Apartments', 'Studio, $895', '1029 Geary St. Apartments', 'Bayside Village Apartments', '400 Broadway', '979 Sutter Street', 'Beautiful Furnished Rooms in North Beach', 'Beautiful Community Living in SoMa', '118 Trumbull St', '106 Fern St #12', '2475 19th Ave', 'Studio, $1,395', '624 Ellis St #9', '80 Raymond Ave', 'Common City Gardens Apartments', '1114 Sutter St #10', 'Address Not Disclosed', '109 San Diego Ave']
# property_addr_2 = ['Lower Nob Hill, San Francisco, CA', 'Chinatown, San Francisco, CA', 'Tenderloin, San Francisco, CA', 'South Beach, San Francisco, CA', 'North Beach, San Francisco, CA', 'Lower Nob Hill, San Francisco, CA', 'North Beach, San Francisco, CA', 'South of Market, San Francisco, CA', 'Mission Terrace, San Francisco, CA', 'Lower Nob Hill, San Francisco, CA', 'Parkside, San Francisco, CA', 'Tenderloin, San Francisco, CA', 'Tenderloin, San Francisco, CA', 'Visitacion Valley, San Francisco, CA', 'South of Market, San Francisco, CA', 'Lower Nob Hill, San Francisco, CA', 'Daly City, CA', 'Daly City, CA']
# property_links = ['/c/ca/san-francisco/1000-1010-bush-street-1000-1010-bush-st-san-francisco-ca-94109--2379258280', '/c/ca/san-francisco/studio-895-706-kearny-st-san-francisco-ca-94111--2468098141', '/c/ca/san-francisco/1029-geary-st-1029-geary-st-san-francisco-ca-94109--1004214860', '/c/ca/san-francisco/bayside-village-3-bayside-village-pl-san-francisco-ca-94107--2082867438', '/p/ca/san-francisco/400-broadway-san-francisco-ca-94133--2083093886', '/c/ca/san-francisco/979-sutter-street-979-sutter-st-san-francisco-ca-94109--2082892821', '/c/ca/san-francisco/beautiful-furnished-rooms-in-north-beach-371-columbus-ave-san-francisco-ca-94133--2083093624', '/c/ca/san-francisco/beautiful-community-living-in-soma-251-9th-st-san-francisco-ca-94103--2179492561', '/p/ca/san-francisco/118-trumbull-st-san-francisco-ca-94112--1139029200', '/p/ca/san-francisco/106-fern-st-12-san-francisco-ca-94109--2320594935', '/p/ca/san-francisco/2475-19th-ave-san-francisco-ca-94116--2082974408', '/c/ca/san-francisco/studio-1-395-344-ellis-st-san-francisco-ca-94102--2535985289', '/p/ca/san-francisco/624-ellis-st-9-san-francisco-ca-94109--2534978084', '/p/ca/san-francisco/80-raymond-ave-san-francisco-ca-94134--2083109105', '/c/ca/san-francisco/common-city-gardens-333-12th-st-san-francisco-ca-94103--2082848365', '/p/ca/san-francisco/1114-sutter-st-10-san-francisco-ca-94109--2173378859', '/p/ca/daly-city/address-not-disclosed-daly-city-ca-94014--2082638946', '/p/ca/daly-city/109-san-diego-ave-daly-city-ca-94014--2082630745']

property_addresses = []

for i in range(len(property_addr_2)):
    addr_1 = property_addr_1[i]
    addr_2 = property_addr_2[i]

    addr = f"{addr_1}, {addr_2}"
    property_addresses.append(addr)

print(property_addresses)

property_links = []

for i in range(len(property_href)):
    web_url = 'https://www.trulia.com/'
    complete_url = f"{web_url}{property_href[i]}"
    property_links.append(complete_url)

print(property_links)
