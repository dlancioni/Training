import os
os.system("cls")

def solution(N):
    v = bin(N)[2:].strip('0').split('1')
    return max([len(x) for x in v])
print(solution(10409495))


# Notes

# Binary disregard beginning "0b" -> 2: mens starting by two until the end
print(bin(99))
print(bin(99)[2:])

# Special for
arr = [x for x in [1,2,3]]                          # it returns array, note []
[print(len(x)) for x in ["1","22","333"]]            # it returns array, note [] 
s = sum([x for x in [1,2,3]])                       # aggreg function array  
l = len(([x for x in [1,2,3]]))                     # size array
print(s / l)

# strip (trim) remove blank spaces or parametter in both sides of string
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x) 



