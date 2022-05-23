import os
os.system("cls")

# https://docs.python.org/3/library/datetime.html
# https://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/

import time
from datetime import datetime

# difference between 2 days
tuple0 = time.strptime("Sun 29 Nov 1999 00:00:00", "%a %d %b %Y %H:%M:%S")
tuple1 = time.strptime("Sun 30 Nov 1999 00:00:05", "%a %d %b %Y %H:%M:%S")

# convert tuple to datetime
d0 = datetime(*tuple0[0:6])
d1 = datetime(*tuple1[0:6])

diff = abs(int((d1 - d0).total_seconds()))
print("Diff in seconds {} ".format(diff))

# Convert days to date
d2 = datetime(tuple0.tm_year, tuple0.tm_mon, tuple0.tm_mday)
print(d2)



