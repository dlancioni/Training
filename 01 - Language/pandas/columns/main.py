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
tmp = df.copy()
os.system("cls")
print(tmp.columns)
tmp.columns = ["Col1","Col2","Col3","Col4"] # all column
print(tmp.columns)
tmp.rename(columns={"Col1":"Name", "Col2":"Email"}, inplace=True) # specific column 
print(tmp.columns)

# delete columns
del tmp["Col3"]
tmp.pop("Col4")
print(tmp)

# done
os.system("cls")
print(df)

