import os
import numpy as np
import pandas as pd

# Create a dataset
data = {
    "Name": ["Joana Campos","Rafael Costa","Augusto Castro","Maria Clara","Jose Maria"],
    "Level" :["AVP","AVP","VP","D","ED"],
    "Salary":[10000, 9000, 15000, 20000, 50000],    
    "Note":["","","","",""]
}
cols = ["Name", "Level", "Salary", "Note"]
df = pd.DataFrame(data, columns=cols)

# print the dataset
os.system("cls")
print(df)

# Select row or multiple rows
os.system("cls")
print(df.loc[0])        # Individual
print(df.loc[1])        # Individual
print(df.loc[[1,2,3]])  # Multiple
print(df.loc[1:3])      # Range

# Select row and columns
os.system("cls")
print(df.loc[1:3, ["Name", "Level"]])

# using iloc to work with indexes
os.system("cls")
print(df.iloc[1:3, [0, 1]])

# Filtering results
os.system("cls")
print(df[df["Salary"]>8000])
print(df.loc[df["Name"]=="Rafael Costa", ["Name", "Level"]])
print(df.loc[df["Salary"].between(12000, 15000, inclusive=True), ["Name", "Salary"]])
print(df["Salary"].idxmin)
print(df["Salary"].idxmax)
