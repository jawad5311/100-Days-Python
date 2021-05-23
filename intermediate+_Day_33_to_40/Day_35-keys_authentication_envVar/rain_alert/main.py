
import requests
import os
from decouple import config

MY_LAT = config("LAT")
MY_LONG = config("LNG")
# API_KEY = os.environ.get("OWM_API_KEY")
API_KEY = config("API_KEY")
exclude = "current,minutely,daily,alerts"


response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&exclude={exclude}&appid={API_KEY}"
)

print(response.status_code)
response.raise_for_status()
weather_data = response.json()

data_12_hours = weather_data["hourly"][:12]

index = 0

will_rain = False

for _ in data_12_hours:
    rain_code = int(data_12_hours[index]["weather"][0]["id"])
    index += 1
    if rain_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
