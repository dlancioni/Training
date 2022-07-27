# coding=UTF-8

x = {
    "app":
    [
        {"k":"1", "v":"abcde", "c":"used values abcde"},
        {"k":"2", "v":"12345", "c":"used values abcde"}
    ]    
}


setup = x["app"]

def get(id=0):
    for item in setup:
        if item["k"] == str(id):
            return str(item["v"]).strip()

print(get(1))
print(get(2))