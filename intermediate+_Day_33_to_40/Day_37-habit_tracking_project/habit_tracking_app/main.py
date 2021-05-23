
import requests
import decouple

"""
    Following parameters and endpoints are used to create account on pixe.la 
"""
pixela_endpoints = "https://pixe.la/v1/users"
user_parameters = {
    "token": decouple.config('PIXELA_API'),
    "username": decouple.config('USERNAME'),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoints, json=user_parameters)
# print(response.text)
# print(response.status_code)








