# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
import os
import string
os.system("cls")

def index_for(letter):
    return ord(letter) + 1 - 97 # base 1
def char_at(index):
    return chr(index-1 + 97) # base 1


def solve(n, k):
   string = ""
   while n > 0:
      letter = min(26, k-n+1)
      string += chr(letter + ord('a') - 1)
      k -= letter
      n -= 1
   return string[::-1]

n = 4
k = 6 
#print(solve(n, k))


print(chr(31))
