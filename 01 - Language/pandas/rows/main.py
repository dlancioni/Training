import os
import pandas as pd
import sys

# General setup
pd.set_option("display.precision", 2)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 25)

sep = ";"
path = sys.path[0] + "\\data.csv"
ds = pd.read_csv(path, sep)

# print the dataset
os.system("cls")
print(ds)

# Select row or multiple rows
os.system("cls")
print(ds.loc[0])        # Individual
print(ds.loc[1])        # Individual
print(ds.loc[[1,3,5]])  # Multiple
print(ds.loc[1:3])      # Range

# Select row and columns
os.system("cls")
print(ds.loc[1:3, ["Name", "Level"]])

# using iloc to work with indexes
os.system("cls")
print(ds.iloc[1:3, [0, 1]])

# Filtering results
os.system("cls")
print(ds[ds["Salary"]>8000])
print(ds.loc[ds["Name"]=="Rafael Costa", ["Name", "Level"]])
print(ds.loc[ds["Salary"].between(4000, 6000, inclusive=True), ["Name", "Salary"]])
print(ds["Salary"].idxmin)
print(ds["Salary"].idxmax)
