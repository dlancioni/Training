# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np
#
# Create arrays to given shape, dtype and order
#
os.system("cls")
data = np.empty([2,2], dtype=np.int32)
print(data) # contents are handle values

os.system("cls")
data = np.zeros([3,3], dtype=np.int32)
print(data) # filled with zeros

os.system("cls")
data = np.ones([3,3], dtype=np.int32)
print(data) # filled with zeros

#
# Create arrays based in other array
#
os.system("cls")
arr = [1,2,3]
print(np.asarray(arr, dtype=np.int32))
print(np.asarray(arr, dtype=np.float32))

#
# Create arrays from iterators
#
os.system("cls")
list = range(10)
it = iter(list)
print(np.fromiter(it, dtype=np.int32))

#
# Create arrays from strings
#
os.system("cls")
prices = "1.11 - 2.22 - 3.33"
print(np.fromstring(prices, dtype=np.float32, sep="-"))

