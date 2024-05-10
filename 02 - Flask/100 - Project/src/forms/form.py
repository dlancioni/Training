# used to demo how bind request data to class
class Form(dict):
   def __init__(self):
      self.validated = True
      self.message = ""