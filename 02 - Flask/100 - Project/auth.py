from flask import Blueprint, render_template, request
from src.forms.login import Login

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
   
   # do not avoid get request to save data
   if request.method == "POST":
      form = Login(** request.form)
      form.validate()
      if form.validated:
        return render_template('main.html')
      else:
         return render_template('login.html', form=form)