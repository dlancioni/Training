# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np

os.system("cls")
x = np.array([1,2,3])
y = np.array([10,20,30])
print(x + y)
print(y - x)
print(y * x)
print(y / x)

os.system("cls")
a = np.array([   [1,2,3], [4,5,6], [7,8,9]   ])
b = np.array([   [1,2,3]   ])
print("------- x")
print(a)
print("------- y")
print(b)
print("------- multiply")
print(a+b)
