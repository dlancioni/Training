from datetime import datetime
import time


# 2 digit [y]ear
now = datetime.now()

# nao funciona
print(time.strftime("%Y-%m-%d %H:%M:%S", now))

# funciona
print(time.strftime("%Y-%m-%d %H:%M:%S", now.timetuple()))