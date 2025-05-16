import pandas as pd

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

"""
   calories  duration
0       420        50
1       380        40
2       390        45
"""

# locate row
# to locate one specific row:
print(df.loc[0])

# to return 0 and 1
print(df.loc[[0, 1]])

idf = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(idf)

print(idf.loc["day2"])

# load file into a dataframe
person_df = pd.read_csv("people.csv")
print(person_df)
