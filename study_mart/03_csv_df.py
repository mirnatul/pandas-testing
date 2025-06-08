import pandas as pd

# importing excel file (csv file)
df = pd.read_csv("Screen Time Data.csv")

# for excel - read_excel('file name.xlsx')

print(df)

# just give the list column name
print(df.columns)
# will just give the values (by nd array)
print(df.values)


# see a particular column
# df.column_name
print(df.Date)
# for space
print(df[["Week Day"]])
# multiple column - we can also add head tail etc here
print(df[["Date", "Week Day"]])
print(df[["Date", "Week Day"]].head(3))

# by default we don't need to put the ascending term
# sort the full dataset but sort with a specific column
print(df.sort_values("Date", ascending=False))

# show and sort a particular column
print(df["Date"].sort_values(ascending=False))
