import os
import json
os.system("cls")

# reading the data from file
with open("c:\\temp\\dictionary.txt") as f:
    data = f.read()
data = json.loads(data)    

# navigate the dict
print( data["Side 1"]["Datasource"][0]["Name"] )

# check tag exists
print( "Side 1" in data )
print( "Field" in data["Side 2"]["Datasource"][0] )

# size
print(len(data["Side 1"]["Datasource"]))

# iterate
for datasource in data["Side 1"]["Datasource"]:
    for field in datasource["Field"]:
        print(field)
        
        
def get_field_type(key=""):
    types = {
        "integer": "Integer",
        "decimal": "Real",
        "text": "Text",
        "datetime": "Text",
    }
    return types.get(key)

print( get_field_type("decimal") ) 


def get_field_list(fields=[], types=None, funcs=None):
    i = 0
    sql = ""
    if fields == []: return ""
    size = len(fields) -1
    while i <= size:
        name = fields[i]
        func = funcs[i] if funcs != None else ""
        sql += f"{func}({name}) {name}, " if func else f"{name}, "
        i += 1
    sql = sql.strip()[:-1]    
    return sql

os.system("cls")
fields = ["account", "balance"]
types = ["text", "decimal"]
aggregs = ["", "sum"]
print( "Select: ", get_field_list(fields, types, aggregs) )
                
fields = ["account", "balance"]
print( "Order By: ", get_field_list(fields) )
    
print( "Order By: ", get_field_list() )    
    
    
dect =  {
    "Id": 1,
    "Name": "Saldo x Extrato",
    "Side 1":
    {
        "Name": "Balance",
        "Datasource":
        [
            {
                "Name": "Sybase 1",
                "Table": "tb_balance",
                "Key": ["account"],
                "Field": ["account", "balance"],
                "Type": ["text", "decimal"],
                "Aggregation": ["", "sum"],
            }
        ]
    },
    "Side 2":
    {
        "Name": "Statement",
        "Datasource":
        [
            {
                "Name": "Sybase 1",
                "Table": "tb_statement",
                "Key": ["account"],
                "Field": ["date", "account", "balance"],
                "Type": ["datetime", "text", "decimal"],
                "Aggregation": ["", "", "sum"],
            }
        ]
    }
}