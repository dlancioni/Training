import os
from time import time
from datetime import datetime
os.system("cls")

# print current time
def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
    

#generate a text file and save it in the same directory
def generate_text_file():
    with open("c:\\temp\\bigfile.txt", "w") as f:
        for i in range(1, 50000000):
            f.write("This is line %d\n" % (i))

print(current_time())
#generate_text_file()            
print(current_time())
print("Done")

# difference between start time and end time
def difftime(start, end):
    return end - start




