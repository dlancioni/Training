import os
import datetime
import pendulum as pdl
os.system("cls || clear")

# is valid date
dt = pdl.datetime(2022, 2, 15)
print(isinstance(dt, datetime.datetime))

# parsing
dt = pdl.from_format("2022-11-05 22:30:59", "YYYY-MM-DD HH:mm:SS")
print(dt.format("YYYY-MM-DD HH:mm:SS"))

# printing
dt = pdl.datetime(1975, 12, 25, 14, 15, 16)
print( dt.to_date_string() )
print( dt.to_time_string() )
print(dt.format("DD/MM/YYYY HH:mm:SS"))
print(dt.format("YYYY-MM-DD HH:mm:SS"))
