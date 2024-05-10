from src.forms.form import Form

class Login(Form):

   def __init__(self, username="", password=""):

      # form fields
      self.username = username
      self.password = password

      # validation message per field
      self.username_err = ""      
      self.password_err = ""

   def __str__(self):
      return f"{self.username} {self.password}"
   
   def validate(self):
      if self.username.strip() == "":
         self.username_err = "Campo Obrigatório"
         Form.validated = False
      if self.password.strip() == "":
         self.password_err = "Campo Obrigatório"
         Form.validated = False