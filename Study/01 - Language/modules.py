# https://docs.python.org/3/tutorial/modules.html

import sys

# Add to pythonpath
sys.path.append("util/string/")

#from util.string.stringfunc import trim
from stringfunc import trim

# Using a lib from [[util/string]]/stringfunc
print(trim("  david  ")) 

# Show imported function (which names the module defines)
print(dir()) 
print(dir("stringfunc"))

