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
data = np.array([ [11,12,13],[21,22,23] ]) # shape 2L
print(data[0])
print(data[0][0])