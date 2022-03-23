# https://leetcode.com/problemset/all/
import os
os.system("cls")

def rotate(arr, cycle):
    for i in range(cycle):
        last = arr[-1]
        for j in reversed(range(len(arr))):
            arr[j] = arr[j-1]
        arr[0] = last
    return arr
    

arr = ["a", "b", "c", "d", "e"]
print(rotate(arr, 5))



