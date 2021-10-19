# https://www.w3schools.com/python/python_dictionaries.asp

# Sintaxe using {}
dict1 = {"k1":"v1", "k2":"v2", "subkey": ["sub1", "sub2", "sub3"]}

# Sintaxe using dict
dict2 = dict([("k1", "v1"), ("k2","v2")])

# Nested dict
dict3 = {
  "k1" : {
    "v1" : "Emil",
    "v2" : 2004
  },
  "k2" : {
    "v1" : "Tobias",
    "v2" : 2007
  }
}

# Add or change items
dict1["k3"] = "v3"
dict1.update({"k4":"v4"})

# Print basic info
print(dict1)
print(type(dict1))                    # type <class 'dict'>
print(dict1["k1"])                    # pair value
print(dict1.get("k2", "not found"))   # return value or string if not found (or exception)
print(dict1["subkey"])                # subkeys 
print(dict1["subkey"][0])             # subkey
print(len(dict1.get("k1")))           # size
print(isinstance(dict1, dict))        # Test type

# Get keys/values/items
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# iterate over
for x, y in dict1.items():
    print(x, y)

# Check if tag exists
if "k1" in dict1:
    print("k1 is a valid tag")

# Remove items
dict4 = {"k1":"v1", "k2":"v2", "k3":"v3"}
print(dict4.pop("k99", "not found"))         # not found or exception  
print(dict4.pop("k1"))                       # return removed value v1
dict4.popitem()                              # remove last item k3/v3
print(dict4)


