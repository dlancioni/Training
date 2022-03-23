# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
import os
import string
os.system("cls")

def index_for(letter):
    return ord(letter) + 1 - 97 # base 1
print(index_for("k"))

def char_at(index):
    return chr(index-1 + 97) # base 1
#print(char_at(1))


