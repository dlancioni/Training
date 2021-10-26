# https://www.tutorialspoint.com/python/python_files_io.htm
# https://www.tutorialspoint.com/python/file_methods.htm

import os
from os.path import exists
os.system("cls")

# Delete current file
if exists("file.txt"):
    os.remove("file.txt")

# create file
f1 = open("file.txt", "w+")  # Read append (cursor EOF)

# write to the file
f1.write("David Lancioni\n")
f1.write("David Lancioni\n")
f1.write("David Lancioni\n")

# Check current position
print("Current position: ")
print(f1.tell())

# Reposition the cursor to beginning of file
position = f1.seek(0, 0)

f1.close()

# File attributes
print(f1.name)      # file.txt
print(f1.closed)    # false
print(f1.mode)      # a+

# Read file contents
f1 = open("file.txt", "r")  # Read only (cursor BOF)
text = f1.read()
print(text)
f1.close()

# Iterate over file
with open("file.txt", "r") as f1:
    for line in f1:
        x = line.strip()
        print(x[0:5].strip())

