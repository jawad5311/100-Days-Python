

import pandas


# Reading data using pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])  # Reading data from "temp" column

# temp_list = data["temp"].to_list()
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
#
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Accessing data of the row with high temp
print(data[data.temp == data.temp.max()])


# # Accessing data from row "Monday" and converting its temp value from C to F
# monday = data[data.day == "Monday"]
# monday_temp_f = (monday.temp * 9/5) + 32
# print(monday_temp_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
