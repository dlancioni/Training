# https://www.w3schools.com/python/python_ref_functions.asp

import os
os.system("cls")

# General useful functions
print(abs(-100))

# Check if all items are true
print(all([1, 1, 1]))     # True list
print(all([1, 1, 0]))     # False list
print(all({1, 1, 1}))     # True set
print(all({1: "Apple", 2: "Orange"}))     # False dictionary

# Check if at least one items is true
print(any([0, 0]))     # False
print(any([0, 1]))     # True

# Check if object is callable
x = 0
def fn():
    pass    
print(callable(x))      # False
print(callable(fn))     # True (you can call a function)

# Execute code in runtime (see mode eval, exec, single)
x = compile('print(55)', 'test', 'eval')
exec(x)

# Return (tuple) quotient and remainder
print(divmod(5, 2))

# Create an iterator
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# Create a range of numbers
x = reversed(range(1,5))  
print(next(x))  # 4
print(next(x))  # 2


