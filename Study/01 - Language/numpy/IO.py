# https://numpy.org/devdocs/reference/generated/numpy.loadtxt.html
import os
import numpy as np

# use npy format
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(3, 3)
os.system("cls")
np.save("c:\\temp\\io", data)
data = np.load("c:\\temp\\io.npy")
print(data)

# save array as a simple text file
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).reshape(3, 3)
os.system("cls")
np.savetxt("c:\\temp\\io.txt", data, fmt="%d")
data = np.loadtxt("c:\\temp\\io.txt", dtype=int)
print(data)

