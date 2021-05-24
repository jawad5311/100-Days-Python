
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
graph_id = "graph1"

graph_parameters = {
    "id": graph_id,
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

post_pix_endpoint = f"https://pixe.la/v1/users/jawad5311/graphs/{graph_id}/"

pixel_parameters = {
    "date":"20210522",
    "quantity":"7",
    "optionalData":"{\"work\":\"Trading Alert App\"}"
}

post_pixel = requests.post(
    url=post_pix_endpoint,
    headers= headers,
    json= pixel_parameters
)

print(post_pixel.status_code)
print(post_pixel.text)

