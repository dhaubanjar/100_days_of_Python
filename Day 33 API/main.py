""" This program sends email to me from myself if the International satellite is above me in the sky, and it is a
nighttime"""

import requests
from datetime import datetime
import password
import smtplib
import time

MY_LAT = 33.60951580586492
MY_LONG = -101.8909205423158

""" function to get sunrise and sunset values from API"""

def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params={"lat": MY_LAT, "lng": MY_LONG, "date": 2024-12-5, "formatted": 0} )
    response.raise_for_status()
    data = response.json()

    # sunrise and sunset
    sunrise = int(data.get("results").get("sunrise").split("T")[1].split(":")[0])
    sunset = int(data.get("results").get("sunset").split("T")[1].split(":")[0])
    time_now = datetime.now()


    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

""" function to get lat and lng values of ISS using API """

def is_satellite_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    satellite_lat =float(data.get("iss_position").get("latitude"))
    satellite_long = float(data.get("iss_position").get("longitude"))

    if MY_LAT +5 <= satellite_lat <= MY_LAT +5 and MY_LONG-5 <= satellite_long <= MY_LONG+5 :
        # checks if the lat n lng of satellite is +- 5 of my location
        return True

""" checks if it is a night time and the satellite is above me and sends email if conditions matches"""
while True:
    time.sleep(60)              # refresh every 60 seconds
    if is_night() and is_satellite_above():
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(password.MY_EMAIL, password.MY_PASSWORD)
        connection.sendmail(
            from_addr=password.MY_EMAIL,
            to_addrs=password.MY_EMAIL,
            msg="Subject: Look Up\n\nThe International Satellite is above you in the sky."
        )