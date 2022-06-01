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

#print the columns
os.system("cls")
for col in ds.columns:
    print(col)

# print specific columns
os.system("cls")
print(ds["Salary"])      # Named
print(ds[ds.columns[0]]) # First
print(ds[ds.columns[2]]) # Third
print(ds[ds.columns[ds.columns.size -1]]) # Last

