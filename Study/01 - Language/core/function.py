# https://www.w3schools.com/python/python_functions.asp

# Basic usage
print("Basic usage")
def fn1(x, y):
    return x * y
print(fn1(2, 3))
print(fn1(x=2, y=3))

# Default value returning tuple
print("Default value returning tuple")
def fn2(x=2):
    return 1, x
x, y = fn2()
print(x + y)

# Multiple parameters (become a tuple)
print("Undefined parameters (become a tuple)")
def fn3(*args):
    print(args[0])
    print(args[1])
    print(args[2])
fn3("David", "Coutinho", "Lancioni", "...")

# Unknow parameters (named)
print("Named parameters parameters")
def fn4(**args):
    print(args["firstName"])
    print(args["lastName"])
fn4(firstName="David", lastName="Lancioni")

# Use pass for empty function (no func def)
print("Use pass for empty function (no func def)")
def fn5(**args):
    pass

# Recursive function
print("Recursive function")
def recursion(k):
    if k > 0:
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
recursion(10)
