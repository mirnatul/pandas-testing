import pandas as pd

df = pd.read_csv("data_for_cleaning.csv")

# return 'index Boolean' formate if duplicate give true
# ex: 4 True
print(df.duplicated())

# removing duplicates
df.drop_duplicates(inplace=True)
print(df)
