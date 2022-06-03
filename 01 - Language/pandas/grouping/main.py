import os
import numpy as np
import pandas as pd

# Create a dataset
January = {
    "Name": ["BTC","ETH","BNB","ADA","SOL"],
    "Amount":[10000, 9000, 15000, 20000, 50000],
    "Price":[29000, 1700, 300, 1.00, 40.00],
    "Risk":[1, 2, 2, 4, 4],    
}
cols = ["Name", "Amount", "Price", "Risk"]
df = pd.DataFrame(January, columns=cols)

# aggregating
os.system("cls")
print(df["Price"].agg(["sum"]))
print(df["Price"].agg(["sum", "count"]))


# grouping
os.system("cls")
print(df.groupby(["Risk"]).sum()) # sum all numeric columns
print(df.groupby(["Risk"])["Price", "Amount"].sum()) # pick the columns

# complex
os.system("cls")
aggreg = {"Price": ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'mad', 'prod']}
print(df.groupby(['Risk']).agg(aggreg).round(2))

# sorting values
os.system("cls")
print(df.sort_values(by=["Price"], ascending=True))
print(df.sort_values(by=["Price"], ascending=True).groupby(["Risk"]).agg("sum"))
print(df.sort_values(by=["Price"], ascending=True).groupby(["Risk"])["Amount", "Price"].agg("sum"))

