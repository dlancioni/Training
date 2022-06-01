# https://docs.python.org/3/tutorial/modules.html
import sys
import os
os.system("cls")



# Add to pythonpath
sys.path.append("util/string/")
sys.path.append("util/")

#from util.string.stringfunc import trim
from stringfunc import trim, getA, getB

# Using a lib from [[util/string]]/stringfunc
print(trim("  david  ")) 

# Show imported function (which names the module defines)
print(dir()) 
print(dir("stringfunc"))

# Print data from modules
print(getA()) # from util
print(getB()) # from util/string