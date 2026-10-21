import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(len(data))
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

dict={
    "Furcolor" : ["Gray", "Black", "Cinnamon"],
    "count" : [grey_squirrels_count, black_squirrels_count, Cinnamon_squirrels_count]
}
dict_dataframe = pd.DataFrame(dict)
dict_dataframe.to_csv("squirresl_count.csv")