from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, ValidationError

# this method is globa, you can use in any form
# note you have to use as any other validator (see line 18)
def length(min=-1, max=-1, message=""):
    message = message % (min, max)
    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length

class Form1(FlaskForm):
    firstname = StringField(label=('First Name:'), validators=[InputRequired(message="First name is mandatory")])
    lastname = StringField(label=('Last Name:'), validators=[])
    password = StringField(label=('Password:'), validators=[length(min=2, max=5, message="Password must be %d and %d characteres long")])
    
    submit = SubmitField(label=('Submit'))
    
    # this method is specifically used in field username field
    # note that you dont need to call it anyware
    def validate_lastname(self, field):
        if len(field.data) == 0:
            raise ValidationError("Last name is mandatory")

    
