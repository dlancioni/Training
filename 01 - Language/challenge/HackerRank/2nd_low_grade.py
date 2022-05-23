# https://docs.python.org/3/library/functions.html

import itertools 
import os
os.system("cls")

# list to be ordered
list1 = [["C", 20.0], ["B", 50.0], ["A", 50]]
names = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]
scores = [37.21, 37.21, 37.2, 41, 39]

# 
# Ziping
#
#
def zip1():
    
    #zip() return must be cast to proper structure (dict or tuple)
    tup1 = tuple(zip(names, scores))
    dic1 = dict(zip(names, scores))    
    sort = dict(sorted(zip(names,scores)))

#
# Sorting
#
# order by letter asc and desc
def fn1():
    x = sorted(list1, key=itemgetter(0))
    print(x)

# order by letter asc and desc
def fn2():
    list1.sort(key=lambda x: x[0])
    list1.sort(key=lambda x: x[0], reverse=True)
    print(list1)
    
# order by value
def fn3():
    list1.sort(key=lambda x: x[1])
    list1.sort(key=lambda x: x[1], reverse=True)
    print(list1)
    
#     

# final solution
def final1():
    #for i in range(5):
        #name=input()
        #names.append(name)
        #score=float(input())
        #scores.append(score)
    dic = dict(sorted(zip(names,scores)))

    mini = (min(scores))
    cnt = scores.count(mini)

    for i in range(cnt):
        scores.remove(mini)
        
    minim=min(scores)
    for i,j in dic.items():
        if j==minim:
            print(i)    
            
def final():

    # join the arrays and order asc
    # will use this list to find and print final result
    dict1 = dict(sorted(zip(names, scores)))

    # remove all occurences of minor score
    minor = min(scores)
    count = scores.count(minor)
    for item in range(count):
        scores.remove(minor)

    # print when grade is equals the minor
    minor = min(scores)    
    for x, y in dict1.items():
        if y == minor:
            print(x)

def short():
    dict1 = dict(sorted(zip(names, scores)))
    for item1 in range(scores.count(min(scores))): scores.remove(min(scores))
    [print(x) for x, y in dict1.items() if y == min(scores)]
            
short()
