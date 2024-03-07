# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

# Reading from csv to create a DataFrame
data = pd.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])


# Conversion from DataFrame to Dictionary
# data_dict = data.to_dict()
# print(data_dict)


## Create a Series and convert to List
temp_list = data["temp"].to_list()
print(temp_list)


## Get average temp of a Series    
# average_temp = data["temp"].mean()
# print(average_temp)


## Get max temp of a Series    
# max_temp = data['temp'].max()
# print(max_temp)


## Get data in a row by filtering for a condition and not the title of the column
# print(data[data.day == "Monday"])


## Get row with max temp
# print(data[data.temp == data.temp.max()])


## Create DataFrame from Dictionary
# data_dict = { "students": ["Tom", "John", "Jerry"], "scores": [80, 85, 83] }
# data = pd.DataFrame(data_dict)

## Convert to csv
# data.to_csv("new_data.csv")
# print(data)
