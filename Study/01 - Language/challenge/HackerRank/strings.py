#https://docs.python.org/3/tutorial/introduction.html#strings
#https://stackoverflow.com/questions/11476713/determining-how-many-times-a-substring-occurs-in-a-string-in-python

import os
import re
os.system("cls")

#swap upper case and lower case strings
def swap_case(s):   
    return "".join([k.lower() if k.isupper() else k.upper() for k in (s)])
print(swap_case('HackerRank.com presents "Pythonist 2".'))
print(swap_case('"####david "///lancioni'))

#split and join strings
def split_and_join(line):
    x = line.split(" ")
    y = "-".join(x)
    return y    
print(split_and_join("David Lancioni"))

    
# count number of substrings in the funciton
# string.count() do not overlap
# see example using regex in regex.py
# here lets use traversing logic
def count_substr(string, sub_string):
    pass
