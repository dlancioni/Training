import os
os.system("cls")


a = ["a", "b", "c"]
b = ["a", "d", "c"]

a = []
b = []

print(set(a).difference(b))
print(list(set(a).intersection(b)))

diff = [i for i, j in zip(a, b) if i == j]
print(diff)

