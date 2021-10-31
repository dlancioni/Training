# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_sets_methods.asp
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.

# Create sets
set1 = {"a", "b", "c"}
set2 = set(("d", "e"))

# Access items
for item in set2:
    print(item)

# Add set items
set2.add("f")      # add (unordered)
set1.update(set2)  # merge set1 and set2

# We can mix types once it is iterable
set1 = set()
arr1 = list((1, 2))
tup1 = tuple((3, 4))
set1.update(arr1)
set1.update(tup1)
print(set1)

# Union sets (return new)
set3 = set1.union(set2)
print(set3)

# Remove items
set1.remove(3)
print(set1)

#
# Interesting methods
#

# Difference
set1 = set((1, 2, 3, 4, 5))
set2 = set((1, 2, 3, 6, 7))
set3 = set1.difference(set2) # 4,5 missing in set 2
set4 = set2.difference(set1) # 6,7 missing in set 1
print(set3)
print(set4)

set1 = set((1, 2, 3))
set2 = set((1, 2, 3))
set3 = set1.difference(set2) # no differences size 0
print(len(set3))

# Subset (if set exists)
set1 = set((1, 2))
set2 = set((1, 2, 3))
set3 = set1.issubset(set2)
print(set3)
