import pandas as pd

df = pd.read_csv("data_for_cleaning.csv")

# return a new data frame with no empty cells
new_df = df.dropna()
print(new_df.to_string())


# dropna returns a new DataFrame, and will not change the original
# if we want to change original do dropna(inplace = True)


# if we want to change the original data frames
# will not return but remove from the original dataframe
df.dropna(inplace=True)
print(df)
