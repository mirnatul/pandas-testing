import pandas as pd

df = pd.read_csv("data.csv")

# will print first and last 5 rows
print(df)

# will print the entire dataframe
print(df.to_string())

# 60, if the row is over 60 it print the header and first and last 5 rows
# we can manually set it
print(pd.options.display.max_rows)
