
class Form(dict):
      
   def __init__(self):
      self.id = 0
      self.error = ""
      self.warning = ""

   """
   commom error messages used on crud
   """     
   field_mandatory = "Campo obrigatório"
   field_type_date = "Campo deve ser do tipo data"
   field_type_time = "Campo deve ser do tipo hora"
   field_type_numeric = "Campo deve ser numérico"

   message_method_not_implemented = "Method not implementd"   

   """
   methods to overload for basic crud
   """
   def validate(self):
      return self.message_method_not_implemented
   
   def insert(self):
      return self.message_method_not_implemented

   def update(self):
      return self.message_method_not_implemented

   def delete(self):
      return self.message_method_not_implemented

   def query(self, id):
      return self.message_method_not_implemented