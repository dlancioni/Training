
# Simple For
arr = [1,2,3,4]    
for item in arr:
    print(item)
    if item == 3:
        break

# Read string (print each letter)
for x in "David":
    print(x)

# Iterate 0 to 5
for x in range(6):
    print(x)

# Iterate 2 to 5
for x in range(2, 6):
    print(x)

# Action on finish
for x in range(6):
    print(x)
else:
    print("Finished count 6")    

# Array
for x in [0, 1, 2]:
    print(x)

# Nested
for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        print(x + y)

