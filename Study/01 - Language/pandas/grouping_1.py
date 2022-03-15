# https://www.programiz.com/python-programming/json
import os
import pandas as pd
os.system("cls")

# General setup
pd.set_option("display.precision", 2)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 25)

sep = ";"
path = "c:\\temp\\data.csv"
data = pd.read_csv(path, sep)

# size and count
x = data.groupby("manager").size()
x = data.groupby("manager")["manager"].count()

# grouping 
x = data.groupby("manager")[ ["sales","clients"] ].sum()

# specific group
x = data.groupby("manager").get_group("Albert")

# First, last or specifc position
x = data.groupby("manager").first()
x = data.groupby("manager").last()
x = data.groupby("manager").nth(0)

# dictionary per groups
x = data.groupby("manager").groups

# different aggregation for each column
x = data.groupby('manager').agg(['sum', 'mean'])

# Specifc aggregate function for each column
x = data.groupby("manager").agg( {"store":"count", "sales":"sum", "clients":"mean"} )


print(data)
print(x)