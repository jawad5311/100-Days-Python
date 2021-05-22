
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


response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()
data = response.json()

print(data)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

print(sunrise, "\n",sunset)


time_now = dt.datetime.now()
print(time_now.hour)



