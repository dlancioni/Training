import os
os.system("cls")

def log(fn):
    def wrapper(*args, **kargs):
        result = fn(*args, **kargs)
        print(result)
    return wrapper

@log
def sum(a, b):
    return a+b

x = sum(1, 1)
x = sum(2, 1)
