import os
os.system("cls")

# https://miguendes.me/how-to-use-datetimetimedelta-in-python-with-examples

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta  # pip install python-dateutil

# define date to work
dt = datetime(2021, 12, 1, 0, 0)
tm = datetime.now()

# add/remove hours
print(tm + timedelta(hours =+ 1))
print(tm + timedelta(hours =-1 ))

# Add/remove days
print(dt + timedelta(days =+ 1))
print(dt + timedelta(days =-1 ))

# Add/remove minutes
print(dt + timedelta(minutes =+ 5))
print(dt + timedelta(minutes =- 5))

# Add/remove weeks
print(dt + timedelta(weeks =+ 5))
print(dt + timedelta(weeks =- 5))

# Add/remove months
print(dt + relativedelta(months =+ 5))
print(dt + relativedelta(months =- 5))

# Add/remove years
print(dt + relativedelta(years =+ 5))
print(dt + relativedelta(years =- 5))