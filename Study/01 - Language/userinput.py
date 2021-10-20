import os

# Clear console
os.system("cls")

# Accept user input
x = input("Enter value 1: ")
y = input("Enter value 2: ")

try:

    # Start processing info
    x = int(x)
    y = int(y)

    # Validate input
    if (not type(x) is int) or (not type(y) is int):
        raise ValueError("Error: input parameters must be integer")

    # Create list
    list1 = []
    list1.append(x)
    list1.append(y)

    # Itarate
    for i in range(x, y+1):
        print(i)

    print("Success !!!")

except:
    print("Fail: input values are invalid")

finally:    
    print("Finish")