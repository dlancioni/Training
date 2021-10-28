import os
import threading
from os.path import exists
from datetime import datetime
os.system("cls")

def get_time():
    print(datetime.now().strftime("%H:%M:%S"))


def Write(x, y):
    if exists(x): os.remove(x)
    f1 = open(x, "w+")
    for line in range(1, y):
        f1.write(str(line) + "\n")

threads = []
threads.append(threading.Thread(target=Write, args=("./concurrency/a.txt", 1000000,)))
threads.append(threading.Thread(target=Write, args=("./concurrency/b.txt", 1000000,)))
threads.append(threading.Thread(target=Write, args=("./concurrency/c.txt", 1000000,)))
threads.append(threading.Thread(target=Write, args=("./concurrency/d.txt", 1000000,)))

print("Multithread:")
get_time()
for t in threads:
    print(t.name)
    t.start()
    #t.join()
get_time()    

print("Singlethread:")
get_time()
Write("./concurrency/e.txt", 100)
get_time()

print("Done")