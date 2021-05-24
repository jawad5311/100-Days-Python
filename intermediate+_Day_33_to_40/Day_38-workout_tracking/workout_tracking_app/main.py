
import decouple
import requests

# Constants -> NutritionIX ID and KEY
app_id = decouple.config("APP_ID")
api_key = decouple.config("NUTRITIONix_API")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    #"Content-Type": "application/json"
}

exercise_params = {
    "query": "30 minutes yoga",
    "gender": "male",
    "weight_kg": 67,
    "height_cm": 160,
    "age": 27
}

exercise_response = requests.post(
    exercise_endpoint,
    json=exercise_params,
    headers=exercise_headers
)

print(exercise_response.status_code)
print(exercise_response.text)
print(exercise_response.json())


