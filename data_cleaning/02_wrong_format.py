# wrong formatted data is impossible to analyze
# Either remove row or convert the same format


import pandas as pd

df = pd.read_csv("data_for_cleaning.csv")

df["Date"] = pd.to_datetime(df["Date"], format="mixed")

print(df.to_string())

# if can not convert, then remove the cell
df.dropna(subset=["Date"], inplace=True)
