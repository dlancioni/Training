import os
from itertools import combinations, count, cycle, repeat
from itertools import product, permutations


def solution(arr):
    



#
# Infinite iterators
#
def fn1():
    for i in count(start=0, step=5):
        print(i)

def fn2():
    arr = [1, 2, 3]
    for i in cycle(arr): 
        print(i, end = " ") 

def fn3():
    repeater = repeat(10, 3)
    try:
        print(next(repeater))
        print(next(repeater))
        print(next(repeater))
        print(next(repeater))
    except StopIteration:
        print("Fourth call - only 3 iterations for value 10")    

#
# Combinatory iterators
#

def fn4():
    """ 
    product cartesion (0,1), (0,1) -> (0,0), (0,1), (1,0), (1,1)
    """
    l = list(product([0, 1], [0,1]))
    l = list(product([0, 1], repeat=2)) #same as before
    l = list(product(["a", "b"], ["a", "b"])) #same as before
    l = list(product([0, 1]))
    print(l)

def fn5():
    """ 
    all possible combinations (1,1) -> (1,1), (1,1) 
    based in positons: 1:1, 1:2, 2:1, 2:2
    """
    l = list(permutations([0, 1])) # [0,1], [1,0]    
    print(l)

def fn6():
    """ 
    combinations of [n] items ig givem list [n1, n2, n3...]
    DO NOT combine [1,1][2,2], DO NOT reverse if [1,2] not [2,1]
    """
    for i in combinations([1,2,3], 2):
        print(i)


os.system("cls")       
fn6()