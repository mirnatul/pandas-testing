import pandas as pd

df = pd.read_csv("data_corr.csv")
print(df.corr())
