import os
import re
os.system("cls")

#https://docs.python.org/3/tutorial/introduction.html#strings

# Slicing
x = "David"
print(x[0:1]) #D       first 
print(x[:1])  #D       first
print(x[-1:]) #d       last
print(x[-2:]) #id      two last
print(x[2:4]) #vi      substring
print(x[2:])  #vid     substring 2 until end
print("54321"[::-1])   #revert string

# Formatting
# https://www.w3schools.com/python/ref_string_format.asp
first = "David"
last = "Lancioni"
print(f"My first name is {first} {last}")
print(f"My first name is {first + last}")
print("Dollar price is {} in Brasil".format(5.50))
print("Dollar price is {} and Euro price is {}".format(5.50, 6.40))
print("{0} is age of {1}. {0} is studying now".format("David", 42))
print("I am studying {language}".format(language="Python"))
print("David {:^16} Lancioni". format("Coutinho"))
print(f"David {1+2} Lancioni")
x = """ 
    David 
    Coutinho
    Lancioni
    """
print(x)    

# functions
# https://www.w3schools.com/python/python_ref_string.asp
print("david coutinho lancioni".capitalize())              # first upper
print("david coutinho lancioni".title())                   # first upper for each word in the sentence 
print("david".upper())                                     # all upper 
print("david".lower())                                     # all lowwer
print("David,".endswith(","))                              # false if not found or not exists 
print("I am, I am not".count("am"))                        # number of occurences or zero if not found
print("I am not".find("not"))                              # 5 as it is the position where beggining of string [not] is found 
print("David, David, David".replace("David", "Renata", 2)) # number of occurences or all

# split or join
line = "David Lancioni"
print(line.split(" "))                      # ['David', 'Lancioni']
print("-".join(['David', 'Lancioni']))      # David-Lancioni

print("david coutinho lancioni".split(" "))
print("".join(["a", "b"]))
print("".join(map(str, [1, 2, 3])))

# string validators
print("aabb!".isalnum())                                   # a-z 0-9 only False 
print("AaBb".isalnum())                                    # a-z 0-9 only True

print("AaBb1".isalpha())                                   # a-z only False 
print("AaBb!".isalpha())                                   # a-z only False
print("AaBb".isalpha())                                    # a-z only True

print("0123456789!".isdigit())                             # a-z 0-9 only False 
print("0123456789".isdigit())                              # a-z 0-9 only True

print("AbCd".isupper())                                    # False
print("AbCd".islower())                                    # False
print("#!%".islower())                                     # False



# change caracteres in string
# must convert to list or slice
def replace_char(string, position, character):
    l = list(string)
    l[position] = character
    output = "".join(l)
    return output

print(replace_char("abracadabra", 5, "k"))
    
# count number of substrings in the funciton
# string.count() do not overlap
def count_substr(string, sub_string):
    pattern = "(?=_)".replace("_", sub_string)
    total = len(re.findall((pattern), string))
    return total

print(count_substr("ABCDCDC", "CDC"))




s= "qA2"
print(True) if s.isalnum() else print(False)
print(True) if s.isalpha() else print(False)
print(True) if s.isdigit() else print(False)
print(True) if s.islower() else print(False)
print(True) if s.isupper() else print(False)