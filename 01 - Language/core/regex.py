import os
import re
os.system("cls")
    
# count number of substrings in the funciton
# string.count() do not overlap
def count_substr(string, sub_string):
    pattern = "(?=_)".replace("_", sub_string)
    total = len(re.findall((pattern), string))
    return total

print(count_substr("ABCDCDC", "CDC"))

