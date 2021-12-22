# https://github.com/italomaia/flask-empty/
# https://programwithus.com/learn/python/pip-virtualenv-windows
# https://flask.palletsprojects.com/en/0.12.x/quickstart/#sessions

users = ["David", "Renata", "Taza"]

from markupsafe import escape
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'  

@app.route('/')
def index():
   return render_template('menu.html')

@app.route('/userdata', methods=["POST", "GET"])
def userdata():
   
   if not "qtt" in session: session["qtt"] = 0
   if not "price" in session: session["price"] = 0
   if not "total" in session: session["total"] = 0

   session["qtt"] = session["qtt"] + 1
   session["price"] = 1.99
   session["total"] = session["price"] * session["qtt"]
   return render_template('userdata.html')

@app.route('/userlist/')
def userlist():
    return render_template('userlist.html', rs=users)

@app.route('/userform/')
def userform():
    return render_template('userform.html', id="", name="")

@app.route("/userform_save", methods=["POST", "GET"])
def userform_save():
   v1 = request.form["id"]
   v2 = request.form["name"]
   return render_template('userform.html', rs=users, id=v1, name=v2)

if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)