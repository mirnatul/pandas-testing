# using mean, median and mode
"""
Mean: the average value
Median: the value in the middle, after sorted
Mode: the value that appears most frequently
"""

import pandas as pd


df = pd.read_csv("data_for_cleaning.csv")

x = df["Calories"].mean()  # or median() or mode()
df.fillna({"Calories": x}, inplace=True)
print(df)
