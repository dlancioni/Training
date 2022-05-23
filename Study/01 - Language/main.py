import os
os.system("cls")

data = {"name":"Argentina", "currency":"Peso", "geo":{"x":"10", "y":"20"}}


def json_parser(dict_var):
    
    for k, v in dict_var.items():
        if isinstance(v, dict):
            for k, v in json_parser(v):
                print(k, v)
        else:
            print(k, v)

json_parser(data)