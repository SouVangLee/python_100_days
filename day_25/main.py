import pandas as pd

# Read csv first
data = pd.read_csv("squirrel_data.csv")

fur_column = data["Primary Fur Color"]
# print(fur_column.filter(["Gray"]).count())
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_count = grey_squirrels["Primary Fur Color"].count()

cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_count = cinnamon_squirrels["Primary Fur Color"].count()

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_count = black_squirrels["Primary Fur Color"].count()

squirrel_color_data = {
    "fur color": ["grey", "cinnamon", "black"],
    "count": [grey_count, cinnamon_count, black_count],
}
new_squirrel_data = pd.DataFrame(squirrel_color_data)
new_squirrel_data.to_csv("color_squirrel_data.csv")


# Easier to count using len
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
