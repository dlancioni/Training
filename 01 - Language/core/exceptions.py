# https://docs.python.org/3/tutorial/errors.html
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions

# Basic flow
print("Basic flow")
def calc():
    return 10/0

try:
    calc()
except Exception as err:
    print("Exception: " + str(err))
else:
    print("Avoid some code on try block")    
finally:
    print("That is it")


# Raise (specific) value error
print("Raise (specific) value error")
try:
    raise ValueError("Problema com valores")
except ValueError as err:
    print("Exception: " + str(err))

