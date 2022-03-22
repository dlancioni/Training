# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import numpy as np

# slice work as start, stop, step
# it is not position + size
# it is position start + position end
# slices are zero based
# can use either slice() or [x:y:z] format
os.system("cls")
data = np.arange(10) # 0...9
print(data[slice(0,1)]) # [0]
print(data[slice(0,2)]) # [0, 1]
print(data[slice(0,3)]) # [0, 1, 2]
print(data[slice(2,4)]) # [2, 3]
print(data[slice(0,10)]) # [0...9]
print(data[slice(0,99)]) # [0...9] no out of bounds error
print(data[slice(0,10,3)]) # [0, 3, 6, 9] we can use STEP

os.system("cls")
print(data[0:1]) # [0]
print(data[0:2]) # [0, 1]
print(data[0:3]) # [0, 1, 2]
print(data[0:10:3]) # [0, 3, 6, 9] we can use STEP

os.system("cls")
data= np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(data[0:1])
print(data[1:2])
print(data[:2])