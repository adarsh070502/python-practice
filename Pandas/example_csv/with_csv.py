import csv

with open(r"/Pandas/Us_states_guessing_game/weather_data.csv") as weathers_file:
    weathers = csv.reader(weathers_file)    # weathers object is created
    temperatures = []
    for row in weathers:       # iterarting through weathers object
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)