import time;
import calendar;
from datetime import datetime
from datetime import timedelta 

x = datetime.now() + timedelta(days=-1)

x = x.strftime("%Y-%m-%d")

print(x)
