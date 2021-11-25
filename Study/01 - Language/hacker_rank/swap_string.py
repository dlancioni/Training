#https://docs.python.org/3/tutorial/introduction.html#strings

import os
os.system("cls")

def swap_case(s):   
    return "".join([k.lower() if k.isupper() else k.upper() for k in (s)])

print(swap_case('HackerRank.com presents "Pythonist 2".'))
print(swap_case('"####david "///lancioni'))

def split_and_join(line):
    x = line.split(" ")
    y = "-".join(x)
    return y 
    
print(split_and_join("David Lancioni"))
