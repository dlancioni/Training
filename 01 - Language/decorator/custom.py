import os
os.system("cls")

def logger(fn):
    def wrapper(*args):
        print(fn.__name__, (args[0]), (args[1]))
        return fn(*args)
    return wrapper

@logger
def sum(a, b):
    return a+b

print(sum(1, 1))

