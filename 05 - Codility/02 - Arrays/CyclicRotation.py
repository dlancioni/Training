import os
os.system("cls")

# Input array
N = ["A","B","C","D"]

# Sizing
print(  len(N)  )       # Size  4
print(  N[0]  )         # First A
print(  N[3]  )         # Last  D

# Slicing
print(  N[:]  )         # [A,B,C,D]
print(  N[0:1]  )       # [A]
print(  N[2:3]  )       # [C]
print(  N[2:4]  )       # [C, D]

# First element
print(  N[:1]  )                        # [A] First element - value
print(  N.index(  N[1]  )  )            # 0   First element - index

# Last element
print(  N[-1:]  )                       # [D]  Last element - value
print(  N.index(  N[-1]  )  )           # 3   First element - index

# using : returns array, otherwise, values
print(  N[0:1] )   #  A
print(  N[0]   )   # [A]

# Count number of occurences
print(  ["A","B","C","B"].count("B")  )

# Reverse 
print(  ["A","B","C","B"].reverse()  )


##############################################################################################
# Final solution
##############################################################################################
os.system("cls")

def solution(A, K):
    if len(A) <= 0: return []
    for i in range(0, K):
        lv = A[-1]
        for j in range( len(A)-1, 0, -1 ):
            A[j] = A[j-1]
        A[0] = lv
    return A

A = [3, 8, 9, 7, 6]
K = 3
print( solution( A, K ) == [9, 7, 6, 3, 8] )

A = [0,0,0]
K = 1
print( solution( A, K ) == [0,0,0] )

A = [1,2,3,4]
K = 4
print( solution( A, K ) == [1,2,3,4] )

A = ""
K = 4
print( solution( A, K )  )