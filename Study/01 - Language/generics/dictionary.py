import os
import re
os.system("cls")

# https://www.w3schools.com/python/python_dictionaries.asp


# Nested dict
products = {
  "1" : {
    "product_id" : "1",
    "product_name" : "produto 1",
    "quantity" : "10",
    "price" : "1.00",
  },
  "2" : {
    "product_id" : "2",
    "product_name" : "produto 2",
    "quantity" : "20",
    "price" : "29.00",
  },
  "3" : {
    "product_id" : "3",
    "product_name" : "produto 3",
    "quantity" : "30",
    "price" : "39.00",
  }  
}

for k, v in products.items():
    item = dict(v)    

product = {
  "4" : {
    "product_id" : "4",
    "product_name" : "produto 4",
    "quantity" : "40",
    "price" : "44.00",
  }
}  
product["price"] = 44.44

# add product
products.update(product)

# get products 1 and 2
prod1 = products.get("1")
prod2 = products.get("2")

# remove a product
products.pop("1")

# iterate over
for k, v in products.items():
    item = dict(v)    
    item['price'] = 0.01
    print(k, v)
    print(item['product_id'])
    print(item['product_name'])
    print(item['quantity'])
    print(item['price'])
type(v)
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


