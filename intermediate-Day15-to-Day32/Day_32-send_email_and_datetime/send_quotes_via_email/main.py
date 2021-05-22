
import smtplib
import random
import datetime as dt

# Opens the quotes files and convert it into py list
with open("quotes.txt") as file:
    quotes = file.readlines()

current_time = dt.datetime.now()  # Holds the current
day = current_time.weekday()  # Holds the current day

# Login Credentials (following credentials are fake)
username = "myemail@gmail.com"
password = "password9012()"

# If the current day is Monday then it will send the quote
if day == 0:
    quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Encrypts the email data
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=username,
            to_addrs="reciever@gmail.com",
            msg=f"Subject: Quote of the Day \n\n Monday quote:\n{quote}"
        )