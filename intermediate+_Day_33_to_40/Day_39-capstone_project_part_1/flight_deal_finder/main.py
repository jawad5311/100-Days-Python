
# Required modules
import os
from datetime import datetime, timedelta

# Project Files
import flight_search
import data_manager
import notification_manager

import dotenv
dotenv.load_dotenv()  # Loads .env file

# Objects created from classes
data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
notification_manager = notification_manager.NotificationManager()

sheet_data = data_manager.get_destination_data()  # Sheet data from Google Sheet

ORIGIN_CITY_IATA = "LON"  # Default location iataCode

# Time format DD:MM:YY
current_time = datetime.now()
from_date = (current_time + timedelta(days=3)).strftime('%d/%m/%Y')
to_date = (current_time + timedelta(days=180)).strftime('%d/%m/%Y')

# Go through each destination from the data and search for fare
for destination in sheet_data:
    flight = flight_search.search_fare_price(
        origin_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_date=from_date,
        to_date=to_date
    )

    if flight is None:
        continue

    # If the fare price is lowest then the actual price then sends an email
    if flight.price < destination['lowestPrice']:
        message = f"From: {flight.origin_city} to {flight.destination_city}\nPrice: {flight.price}\n"

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            notification_manager.send_email(message)
            print(f"Flight with {flight.stop_overs} stops.")

