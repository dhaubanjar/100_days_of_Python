import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
GENDER = os.getenv("MY_GENDER")
WEIGHT_KG = os.getenv("MY_WEIGHT")
HEIGHT_CM = os.getenv("MY_HEIGHT")
AGE = os.getenv("MY_AGE")
BEAR_TOKEN = os.getenv("BEARER_TOKEN")

SYNDIGO_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/15561209459c28cc04375d00e688f1c1/workoutTracking/sheet1"
nutrition_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_text = input("Tell me which exercise you did: ")
exercise_duration = input("Tell me the duration of the exercise: ")
exercise_calories = input("Tell me the calories burn: ")


nutrition_parameter = {
    "query" : exercise_text,
}


# response = requests.post(SYNDIGO_ENDPOINT, json= nutrition_parameter, headers= nutrition_headers)
# response.raise_for_status()
# my_data = response.json()
# print(my_data)

today_date =datetime.now().strftime("%m/%d/%Y")
today_time = datetime.now().strftime("%X")


""" Adding row on google sheet using sheety API """
sheety_headers = {
    "Content-Type": "application/json",
}

""" Adding Bearer Authentication"""
bearer_headers = {
    "Authorization": f"Bearer {BEAR_TOKEN}"
}

""" Column items to be posted in the google sheets. Sheet1 is the name of my workout in sheety.com"""
sheety_parameters = {
    "sheet1" :{
        "date" : today_date,
        "time" : today_time,
        "exercise" : exercise_text.title(),
        "duration" : exercise_duration,
        "calories" : exercise_calories,
    }
}

""" calling POST request to post data into google sheets using sheety API """
add_row = requests.post(SHEETY_POST_ENDPOINT, json= sheety_parameters, headers=bearer_headers)
print(add_row.text)