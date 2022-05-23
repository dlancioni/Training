# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import sys
import numpy as np

#
# range in steps 
#
os.system("cls")
print(np.arange(5, dtype=np.int32))           # [0,1,2,3,4]
print(np.arange(1, 10, 2, dtype=np.int32))    # [1,3,5,7,9]
print(np.arange(1, 10, 5, dtype=np.int32))    # [1,6]

#
# Create arrays to given shape, dtype and order
#
os.system("cls")
print(np.linspace(10, 20, 5, dtype=np.float32))    # [10, 12.5, 15, 17.5, 20] ->see 5 is divided in 2.5 for each item

os.system("cls")
print(np.linspace(10, 20, 5, retstep=True))        # point 2.5 as above example

#
# Pending better understanding
#
os.system("cls")
#print(np.logspace(1.0, 2.0, num = 10)) 
print(np.logspace(10, 20, num = 10)) 
