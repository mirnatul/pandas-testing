# try to replace it, if not possible then remove the cell
# for small data set we can work with one by one, but for large dataset we will work with one by one

import pandas as pd

df = pd.read_csv("data_for_cleaning.csv")


df.loc[7, "Duration"] = 45

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

print(df)
