import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)
print(myvar)
"""
Output:
0    1
1    7
2    2
"""


print(myvar[0])  # 1
