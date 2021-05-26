
import requests
import os
import dotenv
dotenv.load_dotenv()

sheety_endpoint = os.environ.get('SHEETY_USER_ENDPOINT')
sheety_api = os.environ.get('SHEETY_USER_API')
sheety_header = {
    'Authorization': f"Bearer {sheety_api}"
}


# response = requests.get(
#     url=sheety_endpoint,
#     headers=sheety_header,
# )
#
# print(response.json())

user_FN = input(f"Your First Name? ").title()
user_LN = input(f"Your Last Name? ").title()
user_email = input(f"Your Email? ").lower()
user_email_again = input(f"Type your Email again? ").lower()

if user_email == user_email_again:
    sheety_parameters_post = {
        'user': {
            'firstName': user_FN,
            'lastName': user_LN,
            'email': user_email
        }
    }

    post_response = requests.post(
        url=sheety_endpoint,
        headers=sheety_header,
        json=sheety_parameters_post
    )

    print(post_response.status_code)
    print(post_response.text)
    print(f"\nWelcome to the club")
else:
    print(f"Please enter the right email...")



