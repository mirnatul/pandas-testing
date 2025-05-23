import pandas as pd

df = pd.read_json("data.json")

# same rules as csv
print(df)

print(df.to_string())

# we can load python dictionary as dataframe
