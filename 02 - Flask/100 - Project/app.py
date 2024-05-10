from markupsafe import escape
from flask import Flask, render_template

from modules.users import users
from modules.auth import auth

def setup_blueprints(app):
    app.register_blueprint(users, url_prefix = "/modules")
    app.register_blueprint(auth, url_prefix = "/modules")

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1' 
setup_blueprints(app)

@app.route('/')
def login():
   return render_template('login.html', form="")

if __name__ == '__main__':
   app.run(debug=True)