from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, ValidationError

def length(min=-1, max=-1):
    message = 'Must be between %d and %d characters long.' % (min, max)
    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)
    return _length

class Form1(FlaskForm):
    username = StringField(label=('Username:'), validators=[InputRequired(message="campo obrigatorio")])
    password = StringField(label=('Password:'), validators=[length(min=2, max=5)])
    submit = SubmitField(label=('Submit'))
    
    '''
    def validate_username(self, field):
        if len(field.data) == 0:
            raise ValidationError("Username é obrigatório")
    '''
    
