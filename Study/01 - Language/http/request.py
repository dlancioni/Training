# https://www.programiz.com/python-programming/json
import os
os.system("cls")


import json;
import requests;

url = "http://api.zippopotam.us/us/ma/belmont"
json = requests.get(url).json()

# print document
print(json)

# print tags
print(json["country abbreviation"])

# add tag
json["status"] = "pending"
print(json)

print(json["places"][0]["place name"])
print(json["places"][1]["place name"])

