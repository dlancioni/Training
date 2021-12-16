from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired, ValidationError, email_validator

# Custom validator to be used in any below class (must have sub function)
def length(min=-1, max=-1, message=""):
    message = message % (min, max)
    def _length(self, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length

class Form1(FlaskForm):    
    firstname = StringField(label=("First Name:"), validators=[InputRequired(message="First name is mandatory")])
    lastname = StringField(label=("Last Name:"), validators=[])
    email = EmailField(label=("Email"), validators=[Email(message="Email field looks incorrent")])
    password = StringField(label=("Password:"), validators=[length(min=2, max=5, message="Password must be %d and %d characteres long")])    
    submit = SubmitField(label=("Submit"))
    
    # in-form field specific validator (note the name validate_[fieldname])
    def validate_lastname(self, field):
        if len(field.data) == 0:
            raise ValidationError("Last name is mandatory")

class Form2(FlaskForm):
    username = StringField(label=("Username:"), validators=[])
    password = PasswordField(label=("Password:"), validators=[length(min=2, max=5, message="Password must be %d and %d characteres long")])    
    submit = SubmitField(label=("Submit"))

class Form3(FlaskForm):
    country = SelectField("Country:", choices=[("AR","Argentina"), ("BR","Brazil")])
    state = SelectField("State:", choices=[("SP","Sao Paulo"), ("BA","Buenos Aires")])
    submit = SubmitField(label=("Submit"))