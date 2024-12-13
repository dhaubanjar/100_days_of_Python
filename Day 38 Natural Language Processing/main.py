import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SYNDIGO_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameter = {
    "query" : "I ran 1 mile"
}

# response = requests.post(SYNDIGO_ENDPOINT, json= parameter, headers= headers)
# response.raise_for_status()
# data = response.json()
# print(data)

date =datetime.today().date()
time = datetime.today().time().strftime("%H:%M:%S")
print(date)
print(time)