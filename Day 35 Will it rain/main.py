import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
load_dotenv()

""" twilio Account credentials"""
account_sid = os.getenv("WEATHER_ACCOUNT_SID")
auth_token = os.getenv("WEATHER_AUTH_TOKEN")         # saves auth token in environment
api_key = os.getenv("WEATHER_API_KEY")             # saves api key in environment

"""Parameters for API get request"""
parameter ={
    "lat" : 33.609519097242234,
    "lon" : -101.89096661135666,
    "appid" : api_key,
    "cnt" : 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
data = response.json()
weather_data = data

will_rain = False
for data in range(weather_data['cnt']):
    wd = weather_data['list'][data]["weather"][0]["id"]
    if int(wd) == 800:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies={'https': os.getenv("HTTPS_PROXY")}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="BofA: Raj sent you $500.00",
        from_="+18444960152",
        to="+13476014096",
    )
    print(message.status)
