# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np

# Length of each element of arrays IN BYTES
os.system("cls")
print(np.array( [1,2], dtype=np.int8).itemsize)    # 1 byte
print(np.array( [1,2], dtype=np.int16).itemsize)   # 1 byte
print(np.array( [1,2], dtype=np.int32).itemsize)   # 1 byte
print(np.array( [1,2], dtype=np.int64).itemsize)   # 1 byte