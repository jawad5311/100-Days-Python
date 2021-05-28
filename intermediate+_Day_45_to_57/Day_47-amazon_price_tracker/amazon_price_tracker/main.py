
"""
    Amazon Price Tracker

    Tracks the amazon product price and if the product price drops below
    the desired price then send user an email.

"""

import requests
import bs4
import smtplib

import os
import dotenv
dotenv.load_dotenv()  # Loads Environment Variables

desired_price = 40.00  # My desired price to buy this product. 20% less then actual price

url = 'https://www.amazon.com/ELECJET-PowerPie-20000mAh-External-Nintendo/dp/B07YLFX8DT/ref=sr_1_2_sspa?dchild=1&keywords=laptop+power+bank&qid=1622188568&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRldKRUI5WkU4STM5JmVuY3J5cHRlZElkPUEwODA1MzY2MUgwV0tQV0RBOEQzUiZlbmNyeXB0ZWRBZElkPUEwNDQ4MTg5MU0zRkpBNDMxVVpVRCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
# Headers requires to request data from amazon
amazon_headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

response = requests.get(
    url=url,
    headers=amazon_headers
)
print(response.status_code)

# Make soup of the response text
soup = bs4.BeautifulSoup(response.text, 'html.parser')
# Finds the current price and convert it into float
current_price = float(soup.find(
    name='span',
    id='priceblock_ourprice'
).text[1:])

# If the price dropped by the desired price then send email
if current_price < desired_price:
    # Hold the title of the product
    title = soup.find(
        name='span',
        id='productTitle'
    ).text.strip()

    # Make SMTP connection to send email
    with smtplib.SMTP('smtp.live.com') as connection:
        connection.starttls()
        connection.login(
            user=os.getenv('EMAIL'),
            password=os.getenv('PASSWORD')
        )
        connection.sendmail(
            from_addr=os.getenv('EMAIL'),
            to_addrs=os.getenv('USER'),
            msg=f"Subject: Price Drop Alert (Amazon)\n\n"
                f"Price dropped on the following item \n{title}\n"
                f"to ${current_price}"
        )
