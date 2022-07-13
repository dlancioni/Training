# https://pypi.org/project/prettytable/

from prettytable import from_csv
with open("c:\\temp\\data.csv") as fp:
    mytable = from_csv(fp)
print(mytable)    