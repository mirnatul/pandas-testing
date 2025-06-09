import pandas as pd

calories = {"day1": [100, 200], "day2": [100, 200], "day3": [100, 200]}
# myvar = pd.Series(calories)
myvar = pd.DataFrame(calories)
print(myvar)
