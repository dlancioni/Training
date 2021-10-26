# https://www.w3schools.com/python/python_lambda.asp

from functools import reduce
import os
os.system("cls")

# Basic lamba expression (divide 2 numbers)
fn = lambda x, y : x / y
print(fn(10, 2))
fn = lambda x, y : divmod(x, y)
print(fn(10, 2))

# You can return lambda in functions
def fn1(n):
    return lambda a : a * n
fn2 = fn1(2)    # Pass n
print(fn2(5))   # Pass a


# Map using function
v = ("David ", "Coutinho ", "Lancioni ")
def fn(v):
    return len(v)
arr = list(map(fn, v))
print(arr) 

# Map using lambda
v = [1,2,3,4,5]
arr = list(map(lambda x: print(x), v))

# Filter using lambda
v = [1,2,3,4,5]
arr = list(filter(lambda x: x>3, v))
print(arr)

# Reduce using lambda
v = [1,2,3,4,5]
arr = reduce(lambda x, y: x < y, v)
print(arr)

print(max((1, 2, 3)))  # 3
print(max(("David", "Coutinho", "Lancioni")))  # Lancioni