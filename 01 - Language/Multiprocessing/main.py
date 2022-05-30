# https://zetcode.com/python/multiprocessing/
import os
import time
from datetime import datetime
from multiprocessing import Process
os.system("cls")


def fun():
    time.sleep(2)

def main():
    
    to_run = []
    for _ in range(10):
        p = Process(target=fun)
        to_run.append(p);
    


if __name__ == '__main__':
    arr = []
    arr.append(datetime.now().strftime("%H:%M:%S"))
    main()
    arr.append(datetime.now().strftime("%H:%M:%S"))    
    print( arr )
    
    