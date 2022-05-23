import os
os.system("cls")

def log(level):
    def wrap_a(fn):
        def wrap_b(*args, **kargs):
            result = fn(*args, **kargs)
            if (level == 1):
                print("logging calculation: ", result)
            return result    
        return wrap_b
    return wrap_a

@log(level=1)
def sum(a, b):
    return a+b

print(sum(1, 1))



