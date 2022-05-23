# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np

# datatypes
os.system("cls")
print(np.dtype(np.int16))
print(np.dtype(np.int32))
print(np.dtype(np.float32))
print(np.dtype(np.bool8))

# datatypes
os.system("cls")
type = np.dtype([ ("A", np.int8) ])
data = np.array([ (1),(2),(3),(4) ], dtype=type) # shape 2L
print(data["A"][0])    # 1
print(data["A"][1])    # 2
print(data["A"][2])    # 3
print(data.shape)      # (4,) lines and no columns

os.system("cls")
type = np.dtype([ ("A", np.int8), ("B", np.int8) ])
data = np.array([ (1,2),(2,4),(3,6), ], dtype=type) # shape 2L
print(data["B"][0])    # 2
print(data["B"][1])    # 4
print(data["B"][2])    # 6
print(data.shape)      # (3,) lines and no columns

