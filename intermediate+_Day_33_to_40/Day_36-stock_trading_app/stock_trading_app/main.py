
"""
    Stock Trading News Alert App

        Checks for the fluctuation of stock price of Tesla for last 2 days.
        If the there is desired increase of decrease in stocks then
        email the user with top 3 news articles related Tesla.
"""

import requests
import decouple
import smtplib

# Tesla Stock Name and Company name
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API keys
news_api_key = decouple.config('NEWS_API')
stock_api_key = decouple.config('AV_API')

# Endpoint and parameters to fetch data for Tesla
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_api_key
}

# Request stock data with given parameters
stock_response = requests.get(
    url=STOCK_ENDPOINT,
    params=parameters
)

tesla_data = stock_response.json()  # Return stock data into JSON format

# Holds yesterday stock price and day before yesterday stock price and calculates difference
daily_keys = list(tesla_data["Time Series (Daily)"].keys())
yesterday_price = tesla_data["Time Series (Daily)"][daily_keys[0]]["4. close"]
before_yesterday_price = tesla_data["Time Series (Daily)"][daily_keys[1]]["4. close"]
difference = abs(float(yesterday_price) - float(before_yesterday_price))

diff_percent = (difference / float(yesterday_price)) * 100  # Calculate difference percentage

if diff_percent > 1:  # If stock has a difference of 3% then fetch the news and send it to user
    # Endpoint and parameters for news API
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME
    }
    # Response from news api
    news_response = requests.get(
        url=NEWS_ENDPOINT, params=news_params
    )

    all_articles = news_response.json()["articles"]  # Holds all the articles data from JSON file
    index = 0
    for _ in all_articles[:3]:  # Go to first 3 articles from all articles and send mail to user
        headline = all_articles[index]["title"]  # Article headline
        # print(headline)
        desc = all_articles[index]["content"]  # Article Description
        # print(desc)
        index += 1
        # Open connection for the each article and send mail
        with smtplib.SMTP("smtp-mail.outlook.com") as connection:
            connection.starttls()  # Encrypts tha data to be send
            connection.login(  # Login using provided data
                user=decouple.config('MY_EMAIL'),
                password=decouple.config('MY_PASSWORD')
            )
            connection.sendmail(
                from_addr=decouple.config('MY_EMAIL'),
                to_addrs=decouple.config('RECEIVER'),
                msg=f"Subject: Tesla Stock Update\n\n"
                    f"Headline:\n{headline}\nDescription:\n{desc}"
            )
            connection.close()  # Close the connection after sending email
