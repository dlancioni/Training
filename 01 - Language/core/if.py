import os
os.system("cls")

#if statements

x = 20
y = 20

# basic if statement
print("Basic if statement")
if x == y:
    print("X equals Y")
elif x > y:
    print("X greater than Y")
else:    
    print("X smaller than Y")

# same line
print("Same line 1")
if x == y: print("X equals Y")

# short hand
print("Same line 2")
print("Equals") if x == y else print("Different")

# and condition
print("and condition")
if 1==1 and 2==2:
    print("and condition")

# or condition
print("OR Condition")
if 1==1 or 2==2:
    print("or condition")

# empty if
print("Empty if (pass)")
if 1==1:
    pass

# range
x = 2
if x >= 1 and x <= 3:
    print("In range - Easy but long sintaxe")

if 2 in range(1, 3):
    print("In range - easy and less performatic")

if 1 < x < 3:
    print("In range - performatic and short")

if 1 < x < 3:
    print("In range - performatic and short")

if 1 <= x <= 3:
    print("In range - Note the sinal <= to include bounderies")    