
import requests
import decouple
import datetime

"""
    Creating an account on pixe.la 
"""
pixela_user = "jawad5311"
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


"""
    Creating a graph on pixela
"""
graph_endpoint = f"https://pixe.la/v1/users/jawad5311/graphs"
graph_id = "graph1"

graph_parameters = {
    "id": graph_id,
    "name": "Coding_Habit",
    "unit": "min",
    "type": "int",
    "color": "sora",
}

""" Header Token use for authentication."""
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


"""
    Creating pixel on graph
"""
post_pix_endpoint = f"https://pixe.la/v1/users/jawad5311/graphs/{graph_id}/"
today = datetime.datetime.now().strftime("%Y%m%d")

pixel_parameters = {
    "date": today,
    "quantity":"17",
    "optionalData":"{\"work\":\"Trading Alert App\"}"
}
# post_pixel = requests.post(
#     url=post_pix_endpoint,
#     headers= headers,
#     json= pixel_parameters
# )
# print(post_pixel.status_code)
# print(post_pixel.text)


"""
    Updating pixel value using put request
"""
update_pix_endpoint = f"https://pixe.la/v1/users/{pixela_user}/graphs/{graph_id}/{today}"
update_pix_parameters = {
    "quantity": "9"
}
# update_pixel = requests.put(
#     url= update_pix_endpoint,
#     headers= headers,
#     json= update_pix_parameters
# )
# print(update_pixel.status_code)
# print(update_pixel.text)


""" Delete the pixel using delete request """
# delete_pixel = requests.delete(
#     url= f"https://pixe.la/v1/users/{pixela_user}/graphs/{graph_id}/20210522",
#     headers= headers
# )
#
# print(delete_pixel.status_code)
# print(delete_pixel.text)
