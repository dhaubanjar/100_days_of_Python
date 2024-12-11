""" Python Application to send news to the phone if a price of selected stock moves by 5%."""

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests
import os
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

""" Twilio Account Credentials"""
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
api_key1 = os.getenv('STOCK_API_KEY1')             # api for stock portal
api_key2 = os.getenv('NEWS_API_KEY2')             # api for news portal

""" Parameters for stock API """
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": api_key1,
    "outputsize": "compact",
}
response = requests.get(url=STOCK_ENDPOINT, params=parameter)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]         # gets data from API

yesterday_data = stock_data[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = stock_data[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))  # gets difference

diff_percent = (price_difference / float(yesterday_closing_price)) * 100                            # gets percentage

""" For Twilio """
send_text = False
top_news = []
if diff_percent > 5:
    news_parameter = {
        "q": COMPANY_NAME,
        "apikey": api_key2,
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()
    [top_news.append(news) for news in news_data["articles"][: 3]]        # my way using list comprehension
    send_text = True                                                        # sets True if the condition is true

if send_text:   # if send_text = True
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.getenv("HTTPS_PROXY")}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    for news in top_news:
        message = client.messages.create(
            body=f"{COMPANY_NAME} headlines: 🔼 5% : \n Headline: {news["title"]} \n Description: {news['description']}",
            from_="+18444960152",
            to="+13476014096"
        )
        print(message.status)
