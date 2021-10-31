import json;
import requests;

url = "https://jsonplaceholder.typicode.com/todos/1"
json = requests.get(url).json()
print(json)