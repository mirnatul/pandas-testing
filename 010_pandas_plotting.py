# pandas uses the plot() method to create diagrams

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_corr.csv")
df.plot()
plt.show()
