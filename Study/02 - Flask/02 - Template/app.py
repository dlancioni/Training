# https://github.com/italomaia/flask-empty/
# https://programwithus.com/learn/python/pip-virtualenv-windows

users = ["David", "Renata", "Taza"]

from markupsafe import escape
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
   return "welcome !!"

@app.route('/userlist/')
def userlist():
    return render_template('userlist.html', rs=users)

@app.route('/userform/')
def userform():
    return render_template('userform.html', id="", name="")

@app.route("/userform_save", methods=["POST"])
def userform_save():
   v1 = request.form["id"]
   v2 = request.form["name"]
   return render_template('userform.html', rs=users, id=v1, name=v2)

if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)