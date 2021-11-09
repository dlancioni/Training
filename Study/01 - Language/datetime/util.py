import time
import datetime 
import os
os.system("cls")

def seconds(d0, d1):
    diff = d1 - d0  
    diff = diff.total_seconds()
    diff = int(abs(diff))
    return diff

d0 = datetime. datetime(2020, 1, 1, 0, 0, 0)
d1 = datetime. datetime(2020, 1, 1, 0, 0, 5)
print(seconds(d0, d1))

