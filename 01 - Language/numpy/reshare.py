# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np

# datatypes
os.system("cls")
data = np.array([1,2,3,4,5,6,7,8,9])
print(data)
print(data.shape) # 9 lines
print(data.reshape(3,3)) # [1,2,3], [4,5,6], [7,8,9]

os.system("cls")
data = np.array([1,2,3,4,5,6,7,8,9,0])
print(data.reshape(2,5)) # [1,2,3,4,5], [6,7,8,9,0]
print(data.reshape(5,2)) # [1,2], [3,4], ... [9,0]