import time
import os
os.system("cls")

# time ticks (since 70's)
print(time.time())

# time structure or tuple
print(time.localtime(time.time()))

# formatted time based on tuple
print(time.asctime(time.localtime(time.time())))