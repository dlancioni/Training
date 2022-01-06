from flask import Flask
from db.config import db
from db.migrations import create_db

from web.blueprints.user import user
from web.blueprints.category import category
from web.blueprints.store import store

def setup_database(app):
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db.dat"
    db.init_app(app)
    
def setup_blueprints(app):
    app.register_blueprint(store, url_prefix = "/")                 # home page (no prefix ever)
    app.register_blueprint(user, url_prefix = "/admin/user")              # users maintenance
    app.register_blueprint(category, url_prefix = "/admin/category")      # category maintenance

def create_app():
    app = Flask(__name__)
    setup_database(app)
    setup_blueprints(app)
    return app

if __name__ == "__main__":
    app = create_app()
    create_db(app, db)
    app.run()