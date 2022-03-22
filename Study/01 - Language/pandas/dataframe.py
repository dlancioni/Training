# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import pandas as pd
from datetime import datetime

# General setup
pd.set_option("display.precision", 2)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", 25)

# Basic
os.system("cls")
df = pd.DataFrame({"col1":[1,2,3], "col2":["Nome 1", "Nome 2", "Nome 3"], "col3":[1.99, 2.99, 3.99]})
print(df)

# matrix
os.system("cls")
m1 = pd.DataFrame({"col1":[1,2,3]})
m2 = pd.DataFrame({"col1":[1,2,3]})
print(m1)
print(m2)
print(m1 * m2)
