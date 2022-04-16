import os

from sqlalchemy import false
os.system("cls")

def log(fn):
    
    # delegate the function to wrapper
    def wrapper(*args, **kargs):
        
        # do something locally        
        print("before")        
        
        # execute the function passed as parameter
        result = fn(*args, **kargs)
        
        # do something locally        
        print("after")
        
        # logic you can add
        if result == 3:
            return result
        else:
            return 0

    # must return wrapper
    return wrapper

@log
def sum(a, b):
    return a+b

x = sum(1, 1)
x = sum(2, 1)
print('ënd')
