#https://docs.python.org/3/tutorial/introduction.html#strings

import os
os.system("cls")

def swap(v):   
    [print(k[0:1].lower() + k[1:].upper()) for k in v]

#swap([' david"', '"lancioni"'])


print(('"David1'.isalnum()))
print(('"David'.isalpha()))
