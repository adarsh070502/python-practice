import pandas

data = pandas.read_csv("weather_data.csv")

# to print average of temperatures
#print(data["temp"].mean())  # mean is a method in pandas which gives average

# to print max of temperatures
#print(data["temp"].max())

# to get get row data
#print(data[data["day"] == "Monday"])

# to print row data of highest temperature
#highest_temp = data["temp"].max()
#print(data[data["temp"] == highest_temp])

#to covert mondays temperature to farenhiet
monday = data[data["day"] == "Monday"]
print(monday)
tempa = int(monday.temp)
tempa_F = tempa * 9/5 + 32
print(tempa_F)