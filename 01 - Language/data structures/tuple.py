import os
os.system("cls")

# Tuples are ordered (initial order does not change, not possible to sort)
# Tuples are unchangeable, immutable
# Tuples are indexed, so it allows duplicated items
# Important - access items requires at least 1 position [0:0], [1:1], [2:2] does not work. Must use [0:1], [1:2], [2:3]
# If you really need to update a tuple (shouldnt), convert to list, make changes and convert back to tuple

# Tuple example by constructor
t1 = tuple((2,1,2))
t2 = tuple(("David", "Lancioni", 42))
t3 = tuple(("a", "b", "c", "d", "e"))
 
# Tuple type
print(type(t1))         # <class 'tuple'>
print(len(t1))          # tuple size

# Accessing values
print(t2[0])            # David       (0 to get first item)
print(t2[1])            # Lancioni
print(t2[2])            # 42
print(t2[-1])           # 42          (-1 to get last item) 

# Ranges (return a tuple)
tmp = t3[0:0]           # ""
tmp = t3[0:1]           # a
tmp = t3[0:2]           # a, b
tmp = t3[0:3]           # a, b, c
tmp = t3[ :2]           # a, b       (from beggining until 2)
tmp = t3[2: ]           # c, d, e    (from 3 until the end)

# unpacking tuples (must use all 3 tuple items or get exception)
(firstname, lastname, age) = t2

# looping tuples
[print(item) for item in range(len(t3))]    # print indexes
[print(item) for item in t3]                # print values

print("end")