# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
import os
import numpy as np

os.system("cls")
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(3, 3)
    
#     axis 0
#       ^
# 1 2 3 |
# 4 5 6 |
# 7 8 9 |
# -------------> axis 1
print(np.amax(data, 0)) # 7,8,9
print(np.amax(data, 1)) # 3,6,9

# other agregation
os.system("cls")
data = np.array( [1, 2, 3])
print(np.amax(data, 0))
print(np.average(data, 0))


# maximum minus minimun
os.system("cls")
data = np.array( [1, 2, 3, 4, 5, 6, 7])
print(np.ptp(data, 0))
