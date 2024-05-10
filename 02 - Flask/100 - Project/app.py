from markupsafe import escape
from flask import Flask, request, render_template, session

from users import users
from auth import auth

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1' 
app.register_blueprint(users)
app.register_blueprint(auth)

@app.route('/')
def login():
   return render_template('login.html', form="")

if __name__ == '__main__':
   app.run(debug=True)