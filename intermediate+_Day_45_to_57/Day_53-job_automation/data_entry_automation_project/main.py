
import time

import requests
import bs4
from selenium import webdriver

# Request data from zillow.com
response_zillow = requests.get(
    url='https://www.trulia.com/for_rent/San_Francisco,CA/0-1200_price/'
)

print(response_zillow.status_code)  # Return the status of the request

soup = bs4.BeautifulSoup(response_zillow.text, 'html.parser')

# Holds all of the required data from the site
rent_prices = soup.find_all(attrs={"data-testid": "property-price"})
property_address_1 = soup.find_all(attrs={"data-testid": "property-street"})
property_address_2 = soup.find_all(attrs={"data-testid": "property-region"})
links = soup.find_all(name='a', attrs={"data-testid": "property-card-link"})

# Creates the lists of the scrapped data
property_rents = [rent.text for rent in rent_prices]
property_addr_1 = [adr.text for adr in property_address_1]
property_addr_2 = [adr.text for adr in property_address_2]
property_href = [link['href'] for link in links]

# Create a whole single address from the 2 addresses scrapped from the site
property_addresses = []
for i in range(len(property_addr_2)):
    addr_1 = property_addr_1[i]
    addr_2 = property_addr_2[i]

    addr = f"{addr_1}, {addr_2}"  # Combines the street and city address
    property_addresses.append(addr)

# Creates a complete url from of the scrapped incomplete href
property_links = []
for i in range(len(property_href)):
    web_url = 'https://www.trulia.com/'
    complete_url = f"{web_url}{property_href[i]}"  # Adds trulia.com in front of each scrapped link
    property_links.append(complete_url)

# Google form link
form_link = 'https://docs.google.com/forms/d/e/1FAIpQLSftG1mLvbYxRS7citmAKV85gv_Ve2N7ia6ihoTXuMeDoQtFVA/viewform?usp=sf_link'

# Creates and Initialize chrome web driver
driver = webdriver.Chrome('c:/Development/chromedriver.exe')
driver.set_window_size(1300, 720)

# Submits all of the scrapped data to the google form using selenium
for i in range(len(property_addresses)):
    driver.get(form_link)  # Go to the google form link
    time.sleep(1)

    # Get holds of entries and submit buttons
    address_entry = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_entry = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    # Sends the relevant data to its entry column
    address_entry.send_keys('')  # Send an empty string to focus in the entry
    address_entry.send_keys(property_addresses[i])
    rent_entry.send_keys('')  # Send an empty string to focus in the entry
    rent_entry.send_keys(property_rents[i])
    link_entry.send_keys('')  # Send an empty string to focus in the entry
    link_entry.send_keys(property_links[i])

    submit_btn.click()  # Clicks the submit button
    print("From submitted!")

