import pandas as pd

data = pd.read_csv("courses.csv")

print("=== Column Names ===")
print(list(data.columns))

print("\n=== Raw Data Preview ===")
print(data.head())
