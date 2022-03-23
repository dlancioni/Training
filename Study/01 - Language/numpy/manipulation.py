# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np

# reshape
os.system("cls")
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4))
print(arr.reshape(4,2))

# flat view
os.system("cls")
arr = np.array([[1,2], [3,4]])
print(arr.flatten('C'))
print(arr.ravel('C'))

# transpose (2,5 become 5,2)
os.system("cls")
arr = np.arange(10).reshape(2,5)
print("regular:")
print(arr)
print("transposed:")
print(np.transpose(arr))

# roll (rotate array)
os.system("cls")
arr = np.arange(9).reshape(3,3)
print("regular:")
print(arr)
print("roll 1:")
print(np.roll(arr, 3))

# swap axis
os.system("cls")
arr = np.array([[2,3,4]])
print("regular:")
print(arr)
print("swapped:")
print(np.swapaxes(arr, 0, 1))

# concatenate
os.system("cls")
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.concatenate((a,b)))

os.system("cls")
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print("axis 0")
print(np.concatenate((a,b), axis=0))
print("axis 1")
print(np.concatenate((a,b), axis=1))

