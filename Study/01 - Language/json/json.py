# https://www.programiz.com/python-programming/json
import os
os.system("cls")


import json;
import requests;

url = "https://jsonplaceholder.typicode.com/todos/1"
json = requests.get(url).json()

# print document
print(json)

# print tags
print(json["userId"])
print(json["title"])

# add tag
json["status"] = "pending"
print(json)

# add sub level
json["info"] = "{'color'='red', 'value'=22.99}"
print(json)

