# https://www.w3schools.com/python/python_arrays.asp

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
arr2.clear()    
# Insert at the end
arr.append("Honda")     
# Insert at the top or bottom
arr.insert(0, "Tesla")
arr.insert(len(arr), "Dodge")
# Remove at specified positon
arr.pop(0)
# Remove first items with specified value
arr.remove("Dodge")
# count specific items
x = arr.count("Tesla")
# Size of array (base 0)
y = len(arr)
# Reverse the array
arr.reverse()
# iterate over array
for item in arr:
    print(item)
# Multiply array 1,2,3 become 1,2,3,1,2,3
arr = [1,2,3]
arr = arr * 2

# ---------------------------------
# 2D array:
# ---------------------------------

# Basic example
arr = [ [1,2,3], [4,5,6] ]
print(arr)
print(arr[0][1])
for x in arr:
    for y in x:
        print(y)