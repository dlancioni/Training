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

# Insert 
arr.append("Honda")            # first
arr.insert(0, "Tesla")         # first
arr.insert(len(arr), "Dodge")  # last

# Remove 
arr.pop(0)             # at specified positon
arr.remove("Dodge")    # First with specified value

# Other
arr.reverse()                  # reverse 
y = len(arr)                   # size
x = arr.count("Tesla")         # count specific items

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