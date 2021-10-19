# https://www.w3schools.com/python/python_datatypes.asp

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

# Available data types
x = str("Hello World")	                            # str	
x = int(20)	                                        # int	
x = float(20.5)	                                    # float	
x = complex(1j)	                                    # complex	
x = range(6)	                                    # range	
x = bool(5)	                                        # bool	
x = bytes(5)	                                    # bytes	
x = bytearray(5)	                                # bytearray	
x = memoryview(bytes(5))	                        # memoryview
x = frozenset(("apple", "banana", "cherry"))	    # frozenset	

x = list(("apple", "banana", "cherry"))	            # list	
x = ["apple", "banana", "cherry"]

x = tuple(("apple", "banana", "cherry"))	        # tuple	
x = ("apple", "banana", "cherry")

x = dict(name="John", age=36)	                    # dict	
x = {"name" : "John", "age" : 36}

x = set(("apple", "banana", "cherry"))	            # set	
x = {"apple", "banana", "cherry"}

# Casting basic types
x = int(1)      # x will be 1
y = int(2.8)    # y will be 2
z = int("3")    # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


