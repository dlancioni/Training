import time
import os
from functools import cache, lru_cache
os.system("cls")

#@lru_cache(maxsize=5)

@cache
def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


start = time.time()
print(fibonacci(35))
end = time.time()
print(end - start)