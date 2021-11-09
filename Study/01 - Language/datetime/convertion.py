import os
os.system("cls")

# https://docs.python.org/3/library/datetime.html
# https://www.saltycrane.com/blog/2008/11/python-datetime-time-conversions/

import time
from datetime import datetime

# difference between 2 days
x = time.strptime("Sun 29 Nov 1999 00:00:00", "%a %d %b %Y %H:%M:%S")
y = time.strptime("Sun 30 Nov 1999 00:00:01", "%a %d %b %Y %H:%M:%S")

# convert tuple to datetime
d0 = datetime(*x[0:6])
d1 = datetime(*y[0:6])

diff = abs(int((d1 - d0).total_seconds()))
print("Diff in seconds {} ".format(diff))

print((d1.day - d0.day))
print(d1.month - d0.month)
print(d1.year - d0.year)

