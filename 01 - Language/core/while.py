import os
os.system("cls")

# Simple while
i = 0
while i < 10:
    print("Current item: " + str(i))
    i += 1

# While break
i = 0
while i < 10:
    print("Current item: " + str(i))
    i += 1
    if i == 4:
        print("Break on 4")
        break

# Getting in else condition
i = 4
while i < 10:
    print("Current item: " + str(i))
    i += 1    
else:
    print("Greater than 10")


# Simple For
arr = [1,2,3,4]    
for item in arr:
    print(item)
    if item == 3:
        break

# Read string (print each letter)
print("Print each char")
for x in "David":
    print(x)

# Iterate 0 to 5
print("Iterate 0 to 5")
for x in range(6):
    print(x)

# Iterate 2 to 5
print("Iterate 2 to 5")
for x in range(2, 6):
    print(x)

# Action on finish
print("Action on finish")
for x in range(6):
    print(x)
else:
    print("Finished count 6")    

# Array
print("Array")
for x in [0, 1, 2]:
    print(x)

# Nested
print("Nested")
for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        print(x + y)
