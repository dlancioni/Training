import os
os.system("cls")

from datetime import datetime
from datetime import timedelta
import time
import os
os.system("cls")

# time ticks (since 70's)
print(time.time())

# time structure or tuple
print(time.localtime(time.time()))

# formatted time based on tuple
print(time.asctime(time.localtime(time.time())))

# Get diff in seconds
def seconds(d0, d1):
    diff = d1 - d0  
    diff = diff.total_seconds()
    diff = int(abs(diff))
    return diff

d0 = datetime(2020, 1, 1, 0, 0, 0)
d1 = datetime(2020, 1, 1, 0, 0, 5)
#print(seconds(d0, d1))


t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"

t1 = time.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
t2 = time.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

t1 = datetime(*t1[0:6])
t2 = datetime(*t2[0:6])

diff = t2 - t1  
diff = diff.total_seconds()
diff = int(abs(diff))
print (diff)