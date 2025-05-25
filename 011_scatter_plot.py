# we can plot two values x, y by scatter

# in plot
"""
line: by default
scatter: means x, y dot
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_corr.csv")

df.plot()
plt.show()

df.plot(kind="scatter", x="Duration", y="Calories")

# here we see a good relation
plt.show()

df.plot(kind="scatter", x="Duration", y="Maxpulse")
# here we see a bad relation
plt.show()


# histogram to visualize only one column

df["Duration"].plot(kind="hist")
plt.show()
