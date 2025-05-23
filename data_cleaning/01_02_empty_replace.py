import pandas as pd

df = pd.read_csv("data_for_cleaning.csv")

# replace NULL value with the number 130
df.fillna(130, inplace=True)
print(df)

# replace only for specified columns
df = pd.read_csv("data_for_cleaning.csv")
df.fillna({"Calories": 130}, inplace=True)
print(df)
