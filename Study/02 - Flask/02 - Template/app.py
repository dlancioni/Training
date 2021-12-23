# https://github.com/italomaia/flask-empty/
# https://programwithus.com/learn/python/pip-virtualenv-windows
# https://flask.palletsprojects.com/en/0.12.x/quickstart/#sessions

users = ["David", "Renata", "Taza"]

import json
from markupsafe import escape
from flask import Flask, request, render_template, session
app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'

# used to demo how bind request data to class
class User(dict):
   def __init__(self, id, name):
      self.id = id
      self.name = name
   def __str__(self):
      return f"{self.id} {self.name}"      

# home page
@app.route('/')
def index():
   return render_template('menu.html')


@app.route('/userdata', methods=["POST", "GET"])
def userdata():

   # must initialize sessions values   
   if not "qtt" in session: session["qtt"] = 0
   if not "price" in session: session["price"] = 0
   if not "total" in session: session["total"] = 0

   # remember values are stored as cookies
   session["qtt"] = session["qtt"] + 1
   session["price"] = 1.99
   session["total"] = session["price"] * session["qtt"]
   
   # session is visible at template label (no parameters)
   return render_template('userdata.html')

@app.route('/userlist/')
def userlist():
    return render_template('userlist.html', rs=users)

@app.route('/userform/')
def userform():
    return render_template('userform.html', id="", name="")

@app.route("/userform_save", methods=["POST", "GET"])
def userform_save():
   
   # do not avoid get request to save data
   if request.method == "POST":
      
      # demo how to request
      v1 = request.form["id"]
      v2 = request.form["name"]
      
      # request.form is a dict, we can bind with class constructor
      user = User(** request.form)
      
      # could pass the class
      return render_template('userform.html', rs=users, id=user.id, name=user.name)




if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)
   
   
