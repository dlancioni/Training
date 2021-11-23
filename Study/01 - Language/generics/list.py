# https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
# https://www.w3schools.com/python/python_arrays.asp
# https://www.w3schools.com/python/python_arrays.asp

import os
import operator
os.system("clear")

arr = ["Ford", "Volvo", "Volvo"]
arr[2] = "Audi"

'''
print (arr)
print (arr[1])
print (len(arr))
'''

# ---------------------------------
# 1D array:
# ---------------------------------

# Copy
arr2 = arr.copy()

# Clear array
arr.clear()    

# Insert 
# append at the end, insert at specified position
arr.append("Honda")            # first [0]
arr.append("Audi")             # first [1]
arr.insert(0, "Tesla")         # first [move Honda and Audi 1 position down]
arr.insert(len(arr), "Dodge")  # 0-Testa, 1-Honda, 2-Audi, 3-Dodge
arr.pop(2)                     # remove at specified positon (2-audi)
arr.remove("Honda")            # remove at specified value (1-Honda)

# Size related
x = arr.count("Tesla")         # count specific items
y = len(arr)                   # size

# Ordering
arr.reverse()                  # reverse 
arr.sort(key=lambda x: x[0], reverse=True)


# iterate over array
for item in arr:
    print(item)

# Multiply array 1,2,3 become 1,2,3,1,2,3, 1, 2, 3
arr = [1,2,3]
arr = arr * 3
print(arr)

