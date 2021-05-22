import time

import requests
import datetime as dt


# CONSTANTS
MY_LAT = 33.684422
MY_LONG = 73.047882

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

while True:

    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 4
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6

    print(sunrise)
    print(sunset)

    time_now = dt.datetime.now()
    print(time_now.hour)

    if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LONG - 5 < iss_lng < MY_LONG + 5:
        if sunrise > time_now.hour > sunset:
            print("check")

    time.sleep(60.0)

