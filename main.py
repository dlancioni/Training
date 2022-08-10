# coding=UTF-8


field_name = "f @"
valid_char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
invalid_char = ""
for item in field_name:
    if item not in valid_char:
        invalid_char = item
        break
    else:
        print("good")
        print(item)