import os

def json_parser(dict_var):
    for k, v in dict_var.items():
        print(type(k))
        print(type(v))
        if isinstance(v, dict):
            for id_val in json_parser(v):
                print(id_val)
        else:
            print(k, v)                
               
               
                              
# Basic
# dict1 = {'name': 'Jack', 'age': 26}
# os.system("cls")
# json_parser(dict1)

# Complex
dict1 = { 
    "accounting" : 
    [   
        { 
            "firstName" : "John",  
            "lastName"  : "Doe",
            "age"       : 23 
        },
        { 
            "firstName" : "Mary",  
            "lastName"  : "Smith",
            "age"      : 32 
        }
    ],
    "sales": 
    [ 
        { 
            "firstName" : "Sally", 
            "lastName"  : "Green",
            "age"      : 27 
        },
        {  
            "firstName" : "Jim",   
            "lastName"  : "Galley",
            "age"       : 41 
        }
    ] 
}
os.system("cls")
json_parser(dict1)