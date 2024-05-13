from markupsafe import escape
from flask import Flask, render_template

from modules.users import users
from modules.auth import auth
from src.model.config import db, url


def setup_blueprints(app):
    app.register_blueprint(users, url_prefix = "/modules")
    app.register_blueprint(auth, url_prefix = "/modules")

def setup_database(app):
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = url
    db.init_app(app)

def create_app():
   app = Flask(__name__,
                static_url_path="",
                static_folder="web/static",
                template_folder="web/templates")
   app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'    
   setup_blueprints(app)
   setup_database(app)       

if __name__ == '__main__':
   app = create_app()
   app.run(debug=True)