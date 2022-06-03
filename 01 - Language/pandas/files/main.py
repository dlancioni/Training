import os
import pandas as pd
import sys

# general setup
pd.set_option("display.precision", 2)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 25)

# read data file
sep = ";"
path = sys.path[0] + "\\data.csv"
df = pd.read_csv(path, sep)

# print the dataset
os.system("cls")
print(df)
