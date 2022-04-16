import os
os.system("cls")

def log(level):
    def wrap_a(fn):
        def wrap_b(*args, **kargs):
            result = fn(*args, **kargs)
            print(result)
            print(level)
        return wrap_b
    return wrap_a

@log(level=1)
def sum(a, b):
    return a+b

x = sum(1, 1)
x = sum(2, 1)

