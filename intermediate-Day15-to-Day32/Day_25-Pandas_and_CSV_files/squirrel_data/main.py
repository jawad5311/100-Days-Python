
import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

gray_fur_color = data[data["Primary Fur Color"] == "Gray"]
red_fur_color = data[data["Primary Fur Color"] == "Cinnamon"]
black_fur_color = data[data["Primary Fur Color"] == "Black"]

g_fur_count = len(gray_fur_color)
r_fur_count = len(red_fur_color)
b_fur_count = len(black_fur_color)

fur_dict = {
    "fur color": ["gray", "red", "black"],
    "count": [g_fur_count, r_fur_count, b_fur_count]
}

fur_count = pd.DataFrame(fur_dict)

fur_count.to_csv("squirrel_count.csv")
