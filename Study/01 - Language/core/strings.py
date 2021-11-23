import os
os.system("cls")

#https://docs.python.org/3/tutorial/introduction.html#strings

# Slicing
x = "David"
print(x[2:4]) #vi
print(x[:2])  #Da
print(x[2:])  #vid
print("54321"[::-1])

# Formatting
# https://www.w3schools.com/python/ref_string_format.asp
print("Dollar price is {} in Brasil".format(5.50))
print("Dollar price is {} and Euro price is {}".format(5.50, 6.40))
print("{0} is age of {1}. {0} is studying now".format("David", 42))
print("I am studying {language}".format(language="Python"))
print("David {:^16} Lancioni". format("Coutinho"))
print(f"David {1+2} Lancioni")

#Functions
# https://www.w3schools.com/python/python_ref_string.asp
print("David,".endswith(","))
print("".endswith(","))
print("david coutinho lancioni".capitalize())
print("david coutinho lancioni".title())
print("I am, I am not".count("am"))
print("I am not".find(" am"))
print("David, David, David".replace("David", "Renata", 2))
 
t1 =  ("David", "Coutinho", "Lancioni")
x = "; ".join(t1)
print(x)

x = """ 
    David 
    Coutinho
    Lancioni
    """
print(x)    


b = ['a', ' b', 'c ', ' d ']
print(enumerate(b))
for i, s in enumerate(b):
    if s.strip() != b[i]:  # leading or trailing whitespace?
        del b[i]


# upper and capitalize
def capitalize(value, separator):
    arr = value.split(separator)
    arr[:] = [x.capitalize() + " " for x in arr]
    return "".join(arr)

os.system("cls")
x = capitalize("david coutinho lancioni", " ")
print(x)

