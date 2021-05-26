
import smtplib
import os
import dotenv
import requests

dotenv.load_dotenv()

# Email Authentication credentials
user_email = os.environ.get('USER_EMAIL')
user_pass = os.environ.get('USER_PASS')
receiver = os.environ.get('TO_EMAIL')

# SHEETY endpoints, api, & header
sheety_endpoint_user = os.environ.get('SHEETY_EP_USER')
sheety_api = os.environ.get('SHEETY_API')
sheety_header = {
    'Authorization': f'Bearer {sheety_api}'
}


class NotificationManager:
    """ Notify the user with by sending email """
    def send_email(self, msg):
        response = requests.get(
            url=sheety_endpoint_user,
            headers=sheety_header,
        )
        print(response.status_code)
        users = response.json()['users']
        for user in users:
            email = user['email']
            print(email)
            with smtplib.SMTP('smtp-mail.outlook.com') as connection:
                connection.starttls()
                connection.login(
                    user=user_email,
                    password=user_pass
                )
                connection.sendmail(
                    from_addr=user_email,
                    to_addrs=user,
                    msg=msg
                )
                print(f"email send to {user}")


nm = NotificationManager()
nm.send_email("hi")