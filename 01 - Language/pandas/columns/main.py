import os
import pandas as pd
import sys

# General setup
pd.set_option("display.precision", 2)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 25)

sep = ";"
path = sys.path[0] + "\\data.csv"
df = pd.read_csv(path, sep)

# print the dataset
os.system("cls")
print(df)

#print the columns
os.system("cls")
for col in df.columns:
    print(col)

# print specific columns
os.system("cls")
print(df["Salary"])      # Named
print(df[df.columns[0]]) # First
print(df[df.columns[2]]) # Third
print(df[df.columns[df.columns.size -1]]) # Last

# print subset of data (columns)
os.system("cls")
rs1 = df[["Name", "Salary"]]
rs2 = df[[df.columns[0], df.columns[1]]]
print(rs2)

# rename columns
os.system("cls")
print(df.columns)
df.columns = ["Col1","Col2","Col3","Col4","Col5"] # all column
print(df.columns)
df.rename(columns={"Col1":"Name", "Col2":"Email", "Col3":"Hire Date"}, inplace=True) # specific column 
print(df.columns)

# delete columns
del df["Col4"]
df.pop("Col5")

# append columns
df.append()

# done
os.system("cls")
print(df)

