# Info available on __init__.py under util folder
from util import MY_CONSTANT as a
from util.string import MY_CONSTANT as b

def trim(value):
  return str(value).lstrip().rstrip()

def getA():
  return a

def getB():
  return b

