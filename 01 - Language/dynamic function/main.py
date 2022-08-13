# coding=UTF-8

import os
os.system("cls || clear")

# function to variable
def get_value(position, size):
    line = "4;20220404;Text 4;4000.00"
    return line[position:position+size]
fn = get_value
fn(2,8)

# calling function on external text file (put above func def in text file)
f = open("c:\\temp\\fn.py", "r")
fn = f.read()
ns = {}
exec(fn, globals(), ns)
fn, = ns.values()
print(fn(2, 8))