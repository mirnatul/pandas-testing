# head method
# give the header and noted amount of data

import pandas as pd

df = pd.read_csv("data.csv")

# the no number mentioned by default 5 will shown
print(df.head(10))
# same as tail
print(df.tail(10))

# info
print(df.info())

"""
Result analysis:

----- 169 rows and 4 columns
RangeIndex: 169 entries, 0 to 168
Data columns (total 4 columns):

-----the name of each column, with the data type
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
"""

# Null values: Empty values or Null values can be bad when analyzing data, and you should consider removing rows with empty values.
