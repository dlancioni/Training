#if statements

x = 20
y = 20

# Basic if statement
print("Basic if statement")
if x == y:
    print("X equals Y")
elif x > y:
    print("X greater than Y")
else:    
    print("X smaller than Y")

# Same line
print("Same line 1")
if x == y: print("X equals Y")

# Short hand
print("Same line 2")
print("Equals") if x == y else print("Different")

# AND Condition
print("AND Condition")
if 1==1 and 2==2:
    print("and condition")

# OR Condition
print("OR Condition")
if 1==1 or 2==2:
    print("or condition")

# Empty if
print("Empty if")
if 1==1:
    pass