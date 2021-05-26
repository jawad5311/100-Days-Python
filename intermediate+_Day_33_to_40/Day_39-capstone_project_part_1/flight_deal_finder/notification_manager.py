
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
    def send_email(self, msg, link):
        """ Fetch user emails from google sheets and send them flight deals """
        response = requests.get(
            url=sheety_endpoint_user,
            headers=sheety_header,
        )
        print(response.status_code)
        users = response.json()['users']
        for user in users:
            """ Send email to each user individually """
            email = user['email']
            with smtplib.SMTP('smtp.live.com') as connection:
                connection.starttls()
                connection.login(
                    user=user_email,
                    password=user_pass
                )
                connection.sendmail(
                    from_addr=user_email,
                    to_addrs=email,
                    msg=f"Subject: Cheap Flight Alert\n\n{msg}\n\n"
                        f"Book Now: {link}"
                )
                print(f"email send to {user}")
