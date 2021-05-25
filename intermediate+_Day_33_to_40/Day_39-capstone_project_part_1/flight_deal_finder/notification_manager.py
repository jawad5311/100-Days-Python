
import smtplib
import os
import dotenv
dotenv.load_dotenv()

# Email Authentication credentials
user_email = os.environ.get('USER_EMAIL')
user_pass = os.environ.get('USER_PASS')
receiver = os.environ.get('TO_EMAIL')


class NotificationManager:
    """ Notify the user with by sending email """
    def send_email(self, msg):
        with smtplib.SMTP('smtp-mail.outlook.com') as connection:
            connection.starttls()
            connection.login(
                user=user_email,
                password=user_pass
            )
            connection.sendmail(
                from_addr=user_email,
                to_addrs=receiver,
                msg=msg
            )
            print(connection.smtp_code)
