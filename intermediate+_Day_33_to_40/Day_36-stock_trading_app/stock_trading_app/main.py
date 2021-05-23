
import requests
import decouple

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

stock_response = requests.get(
    url=STOCK_ENDPOINT,
    params=parameters
)

tesla_data = stock_response.json()

daily_keys = list(tesla_data["Time Series (Daily)"].keys())


yesterday_price = tesla_data["Time Series (Daily)"][daily_keys[0]]["4. close"]
before_yesterday_price = tesla_data["Time Series (Daily)"][daily_keys[1]]["4. close"]
print(yesterday_price)
print(before_yesterday_price)

difference = abs(float(yesterday_price) - float(before_yesterday_price))
print(difference)

diff_percent = (difference / float(yesterday_price)) * 100
print(diff_percent)

if diff_percent > 1:
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(
        url=NEWS_ENDPOINT, params=news_params
    )

    articles = news_response.json()["articles"]
    # print(articles[:3])
    # print(type(articles))

    first_article = articles[0]
    # print(first_article)

    article_headline = articles[0]["title"]
    print(article_headline)

    article_desc = articles[0]["content"]
    print(article_desc)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and
# each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds 
and prominent investors are required to file by the SEC 
The 13F filings show the funds' and investors' portfolio positions as of 
March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that 
hedge funds and prominent investors are required to file by the SEC 
The 13F filings show the funds' and investors' portfolio positions as of 
March 31st, near the height of the coronavirus market crash.
"""

