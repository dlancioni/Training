# https://www.programiz.com/python-programming/json
import os
import sys
import pandas as pd
from datetime import datetime

# General setup
pd.set_option("display.precision", 2)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 25)

# Import datetime fields
os.system("cls")
sep = ";"
path = sys.path[0] + "\\datatype.csv"
header = ["name", "date"]
date_col = ["date"]
data = pd.read_csv(path, sep=sep, names=header, parse_dates=date_col, dayfirst=True)

# Transform data
os.system("cls")
df = pd.DataFrame({'Date': ['01/03/2018', '06/08/2018', '31/03/2018', '30/04/2018']})    # create data
date_parts = df['Date'].apply(lambda d: pd.Series(int(n) for n in d.split('/')))         # transform
date_parts.columns = ['day', 'month', 'year']                                            # add header
print(date_parts)

# Cast to datetime 
os.system("cls")
data = pd.DataFrame({'Date': ['01/03/2018', '06/08/2018', '31/03/2018', '30/04/2018']})    # create data
data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
print(data)