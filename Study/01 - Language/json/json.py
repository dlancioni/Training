# https://www.programiz.com/python-programming/json
import os
os.system("cls")
import json;

# prepare json string
str = '''
{
    "firstName":"David", 
    "lastName":"Lancioni", 
    "docto":
    [
        {"name":"RG", "value":"11111"},
        {"name":"Cpf", "value":"99999"}
    ]
}
'''

# import json string
dict1 = json.loads(str)

# python handle json as dict
print (isinstance(dict1, dict) )

# print document
print(dict1)

# read tags in first level
print(dict1["firstName"])
print(dict1["lastName"])

# read tags in second level
print(dict1["docto"][0]["name"])
print(dict1["docto"][0]["value"])

# iterating
os.system("cls")
for k, v in dict1.items():
    if isinstance(v, list):
        arr = list(v)
        for item in arr:
            print("    " + item["value"] + " - " + item["value"])
    else:
        print(v)
        
class User(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

str = '''
{
    "firstName":"David", 
    "lastName":"Lancioni"
}
'''

data = json.loads(str)    
user = User(**data)
print(user)    