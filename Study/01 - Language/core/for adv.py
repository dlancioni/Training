import os
os.system("cls")

numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d"]

def fn1():
    print(list(enumerate(letters)))     # index starts on zero (0=a, 1=b)
    print(list(enumerate(letters, 4)))  # index starts on four (4=a, 5=b)     

# create a counter and iterate (very useful)
def fn2():
    for k, v in enumerate(letters):
        print(k, v)
        
# general single line for
def fn3():
    [print(item) for item in numbers]
    [print(item) for item in numbers if item > 3]
    
# print example
def fn4():
    [print(number * 5) for number in numbers]

# transform array
def fn5():
    x = [(number * 5) for number in numbers]
    print(x)

    
fn5()
    
    
