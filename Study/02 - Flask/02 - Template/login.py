# https://programwithus.com/learn/python/pip-virtualenv-windows

from markupsafe import escape
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# http://127.0.0.1:5000/loginform
@app.route('/loginform/')
def loginform():
    return render_template('login.html', p1="", p2="")

# http://127.0.0.1:5000/authentication/david/123
@app.route('/authentication/<string:username>/<string:password>', methods=["GET","POST"] )
def authenticate(username="", password=""):  
   username = escape(username)
   password = escape(password)   
   return render_template('login.html', p1=username, p2=password)

@app.route("/processform", methods=["POST"])
def process_form():
   username = request.form["username"]
   password = request.form["password"]
   return render_template('login.html', p1=username, p2=password)