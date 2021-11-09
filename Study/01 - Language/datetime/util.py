import time
import datetime 
import os
os.system("cls")

# time ticks (since 70's)
print(time.time())

# time structure or tuple
print(time.localtime(time.time()))

# formatted time based on tuple
print(time.asctime(time.localtime(time.time())))


def seconds(d0, d1):

    ''' 
    author: David Lancioni
    step by step do calculate seconds between 2 dates
    '''

    # get long format like 1 day, 0:00:10
    diff = d1 - d0  

    # get result as decimal
    diff = diff.total_seconds()

    # we want int
    diff = int(diff)

    # d0 greater than d1 return negative
    diff = abs(diff)

    # alld one
    return diff

d0 = datetime. datetime(2020, 1, 1, 0, 0, 0)
d1 = datetime. datetime(2020, 1, 1, 0, 0, 5)
print(seconds(d0, d1))

