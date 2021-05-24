
"""
    Workout Tracking App
        Takes user input in Natural Language
        Use NutritionIX api to process input
        Return with workout data
        Saves data into google sheets using Sheety API
"""
import decouple
import requests
import datetime

# Constants -> NutritionIX ID and KEY
app_id = decouple.config("APP_ID")
api_key = decouple.config("NUTRITIONix_API")
exercise_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    # "Content-Type": "application/json"
}

# Sheety KEY and Token
sheety_key = decouple.config("SHEETY_TOKEN")
sheety_header = {
    "Authorization": f"Bearer {sheety_key}",
    "Content-Type": "application/json"
}
# Current Date DD:MM:YY and Time HH:MM:SS
current_date = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# NutritionIX and Sheety Endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/52f8ea1de0e8daa55c2de3b8f338fc44/workouts/workouts"

user_input = input("Tell me about your exercise: ")  # Takes user input in Natural Language

# Exercise parameters to POST request
exercise_params = {
    "query": user_input,
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
print(exercise_response.status_code)  # Prints the status of the request
exercise_result = exercise_response.json()  # Converts the result into json

for exercise in exercise_result["exercises"]:
    add_row = {
        "workout": {
            "date": str(current_date),
            "time": str(current_time),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(
        url= sheety_endpoint,
        headers= sheety_header,
        json= add_row
    )

print(response.status_code)  # Prints the status of the request
