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

# print it
os.system("cls")
print(df)

