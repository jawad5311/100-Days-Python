
import requests
import decouple

"""
    Following parameters and endpoints are used to create account on pixe.la 
"""
pixela_user = decouple.config('USERNAME')
user_token = decouple.config('PIXELA_API')

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": user_token,
    "username": pixela_user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
# print(response.status_code)


graph_endpoint = f"https://pixe.la/v1/users/jawad5311/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Coding_Habit",
    "unit": "min",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": user_token
}

# graph_response = requests.post(
#     url=graph_endpoint,
#     headers=headers,
#     json=graph_parameters
# )

# print(graph_response.status_code)
# print(graph_response.text)





