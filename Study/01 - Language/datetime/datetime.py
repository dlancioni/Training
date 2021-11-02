# https://docs.python.org/3/library/datetime.html
from datetime import datetime
from datetime import timedelta 
from datetime import date

# calculate date
x = datetime.now() + timedelta(days=-1)

# format date output
x = x.strftime("%Y-%m-%d")
print(x)

# create date from integer
print(date(2002, 12, 4).weekday())
