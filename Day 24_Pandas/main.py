import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_gray = len(data[data["Primary Fur Color"] == "Gray"])
fur_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
fur_black = len(data[data["Primary Fur Color"] == "Black"])


new_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [fur_gray, fur_cinnamon, fur_black]
}

df = pandas.DataFrame(new_color_dict)
df.to_csv("Filtered_Colors_Count.csv")