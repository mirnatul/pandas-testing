import pandas as pd

# empty df
df = pd.DataFrame()
print(df)
print(df.info())

city = ["berlin", "munich", "paris"]
df = pd.DataFrame(city, columns=["city_in_Europe"], index=["c1", "c2", "c3"])
"""
   city_in_Europe
c1         berlin
c2         munich
c3          paris
"""
print(df.loc[["c1", "c2"]])
print(df.loc["c1"])
# print(df)
print(df.shape)

# we can add two list using zip
a1 = [1, 2, 3]
a2 = [6, 7, 8]
df = pd.DataFrame(zip(a1, a2), columns=["col1", "col2"])
"""
   col1  col2
0     1     6
1     2     7
2     3     8
"""

print(df)
print(df.info())
print(df.shape)  # (3, 2) showing (row, column)


# 2d array in dataframe
nd = [["math", 100], ["english", 90]]
df4 = pd.DataFrame(nd, columns=["subject", "marks"])
"""
   subject  marks
0     math    100
1  english     90
"""
print(df4)
print(df4.loc[0])
"""
subject    math
marks       100
"""
print(df4.loc[[0, 1]])

# shape
# info
