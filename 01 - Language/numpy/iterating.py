import os
import numpy as np

os.system("cls")
data = np.arange(0, 60, 5) # min, max, step [0, 5, 10, ..., 50, 55]
data = data.reshape(3,4)

for item in np.nditer(data):
    print (data)
