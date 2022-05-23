import os
os.system("cls")

# hash generate a unique (hash) key to given values
# apply for immutable values only (not possible to hash a list for example)

# basic
tmp = hash(1)
tmp = hash("a")
tmp = hash("1a")

# exception, lists are mutable so not possible to get hash
#print(hash([1,2]))

# Classes (note that each class instance has it ows hash)
class Person:
    def __init__(self, name):
        self.name = name
        pass
    def getname(self):
        return f"My name is {self.name}"

p1 = Person("David")
p2 = Person("David")
p3 = Person("Lancioni")

print(hash(p1))
print(hash(p2))
print(hash(p3))

