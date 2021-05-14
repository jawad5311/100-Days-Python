
import csv

# with open("weather_data.csv") as file:
#     weather_data = file.readlines()
#
# print(weather_data)

temperatures = []


with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)





