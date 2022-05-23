from datetime import date
import calendar
import os
os.system("cls")

## print calendar for given year/month
print(calendar.month(2021, 11))

# day_name is an array
print (calendar.day_name[0])
print (calendar.day_name[1])
print (calendar.day_name[2])
print (calendar.day_name[3])
print (calendar.day_name[4])
print (calendar.day_name[5])
print (calendar.day_name[6])

# print day of week of given date
def dayOfWeek(dt):
    # expected string format: MM DD YYYY
    yy = int(dt[6:10])
    mm = int(dt[0:2])
    dd = int(dt[3:5])
    # create date
    dt = date(yy, mm, dd)
    return calendar.day_name[dt.weekday()].upper()

print(dayOfWeek("11 02 2021"))