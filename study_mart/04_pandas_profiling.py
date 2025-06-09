import pandas as pd

# from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport

url = "https://raw.githubusercontent.com/rashakil-ds/Public-Datasets/refs/heads/main/credit.csv"
df = pd.read_csv(url)
print(df.head())

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
print(profile)
# The full profiling report should now appear below the code cell inside your Jupyter Notebook.
print(profile.to_notebook_iframe())

# we can also use this
print(profile.to_file("report.html"))

# it saved the report as an HTML file, we can open it by running
import webbrowser

webbrowser.open("report.html")
