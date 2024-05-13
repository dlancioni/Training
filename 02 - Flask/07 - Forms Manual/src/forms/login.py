from src.forms.form import Form

class Login(Form):

   def __init__(self, username="", password=""):

      """
      mandatory
      """
      self.validated = True

      """
      form fields
      """
      self.username = username
      self.password = password
    
      """
      field validation
      """    
      self.username_err = ""      
      self.password_err = ""

   def __str__(self):
      return f"{self.username} {self.password}"

   """
   inherited methods
   """     
   def validate(self):
      if self.username.strip() == "":
         self.username_err = Form.field_mandatory
         self.validated = False
      if self.password.strip() == "":
         self.password_err = Form.field_mandatory
         self.validated = False