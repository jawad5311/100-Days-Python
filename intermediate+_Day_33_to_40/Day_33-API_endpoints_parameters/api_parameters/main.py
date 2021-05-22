import smtplib
import time
import requests
import datetime as dt


# CONSTANTS
MY_LAT = 33.684422
MY_LONG = 73.047882

# Parameter to request sunrise and sunset data
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

while True:  # This loop will run for every 60 sec
    # Send request and holds ISS lat & long
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])  # ISS latitude
    iss_lng = float(iss_data["iss_position"]["longitude"])  # ISS Longitude

    time_now = dt.datetime.now()  # My current time

    if MY_LAT - 5 < iss_lat < MY_LAT + 5 and MY_LONG - 5 < iss_lng < MY_LONG + 5:
        # If ISS is in my location then it will chech if its day or night in my location
        response = requests.get("https://api.sunrise-sunset.org/json", parameters)
        response.raise_for_status()
        data = response.json()
        # Sunrise and sunset hours
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 4
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6

        if sunrise > time_now.hour > sunset:  # Sends email if it's night
            # with smtplib.SMTP("smtp.gmail.com") as connection:
            #     connection.starttls()
            #     connection.login(
            #         user="myname@email.com",
            #         password="password34-9("
            #     )
            #     connection.sendmail(
            #         from_addr="myname@email.com",
            #         to_addrs="reciever@email.com",
            #         msg="Subject: Watch the SKY\n\n"
            #             "ISS is in moving above Islamabad right now. "
            #             "Go out and try to find it in the sky..."
            #     )
            pass

    time.sleep(60.0)  # Wait for 60 secs
