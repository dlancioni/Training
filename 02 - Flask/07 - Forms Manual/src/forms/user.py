from src.forms.form import Form

class Login(Form):

   def __init__(self, name="", email="", username="", password="", password_new="", password_confirm=""):

      """
      mandatory
      """
      self.validated = True      

      """
      form fields
      """
      self.name = name
      self.email = email
      self.username = username
      self.password = password
      self.password_new = password_new
      self.password_confirm = password_confirm

      """
      field validation
      """  
      self.name_err = ""
      self.email_err = ""
      self.username_err = ""
      self.password_err = ""
      self.password_new = ""
      self.password_confirm = ""

   
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