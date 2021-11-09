import os
os.system("cls")

# https://miguendes.me/how-to-use-datetimetimedelta-in-python-with-examples
# pip install python-dateutil

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


# Add/remove days
print(datetime(2021, 12, 1) + timedelta(days =+ 1))
print(datetime(2021, 12, 1) + timedelta(days =-1 ))

# Add/remove minutes
print(datetime(2021, 12, 1, 0, 0) + timedelta(minutes =+ 5))
print(datetime(2021, 12, 1, 0, 0) + timedelta(minutes =- 5))

# Add/remove weeks
print(datetime(2021, 12, 1, 0, 0) + timedelta(weeks =+ 5))
print(datetime(2021, 12, 1, 0, 0) + timedelta(weeks =- 5))

# Add/remove months
print(datetime(2021, 12, 1, 0, 0) + relativedelta(months =+ 5))
print(datetime(2021, 12, 1, 0, 0) + relativedelta(months =- 5))

# Add/remove years
print(datetime(2021, 12, 1, 0, 0) + relativedelta(years =+ 5))
print(datetime(2021, 12, 1, 0, 0) + relativedelta(years =- 5))