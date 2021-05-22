
import requests

MY_LAT = 47.751076
MY_LONG = -120.740135
API_KEY = "94fb4ed33b056db390dc54823c14f955"
exclude = "current,minutely,daily,alerts"


# parameters = {
#     "lat": MY_LAT,
#     "lon": MY_LONG,
#     "aapid": 94fb4ed33b056db390dc54823c14f955
# }


response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&exclude={exclude}&appid={API_KEY}"
)

print(response.status_code)
response.raise_for_status()
weather_data = response.json()

hourly_data = weather_data["hourly"][:12]

index = 0
id_code = hourly_data[index]["weather"][0]["id"]

will_rain = False

for _ in hourly_data:
    rain_code = int(hourly_data[index]["weather"][0]["id"])
    if rain_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
