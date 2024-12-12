""" Hands-on of POST, PUT, DELETE requests"""

import requests
from datetime import datetime

TOKEN = "abcdefgh"
USERNAME = "ryand"
PIXELA_ENDPOINT = 'https://pixe.la/v1/users/'
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

""" First step is to create account using below code"""
# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

""" Second Step is to request the body """
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}{USERNAME}/graphs"
graph_parameters = {
    "id": "graph111",
    "name": "Walking Graph",
    "unit": "km",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(response.text)

""" Third step is to post a pixel in the graph """
GRAPH_ID = "graph111"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2024, month=12, day=1)
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12",
}

# response = requests.post(PIXELA_ENDPOINT, headers=headers, json=pixel_parameters)
# print(response.text)

""" Fourth step is to update the pixel in the graph """
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_pixel_parameters = {
    "quantity": "5"
}

# response = requests.put(UPDATE_PIXEL_ENDPOINT, headers=headers, json=update_pixel_parameters)
# print(response.text)


""" Fifth step is to delete the pixel in the graph """
DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(DELETE_PIXEL_ENDPOINT, headers=headers)
print(response.text)
