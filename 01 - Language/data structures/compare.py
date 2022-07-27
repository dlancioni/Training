# https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
# https://www.w3schools.com/python/python_arrays.asp
# https://www.w3schools.com/python/python_arrays.asp
# https://www.askpython.com/python/list/find-string-in-list-python (pending read)

import os
import operator
os.system("cls")

# a exists in temp2
temp1 = ["a", "b"]
temp2 = ["a", "b"]

print(set(temp1) - set(temp2))
print(set(temp2) - set(temp1))


temp3 = [item for item in temp1 if item in temp2]
print(temp3)


