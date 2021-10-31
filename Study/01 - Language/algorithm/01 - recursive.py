import os
os.system("cls")

# count down
def fn1(value):
    print(value)
    value -= 1
    if value > 0:
        fn1(value)
    else:
        return
fn1(10)