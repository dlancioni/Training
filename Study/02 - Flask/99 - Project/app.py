from flask import Flask
from modules.user import mod_user
from modules.category import mod_category
from db.config import db
from db.migrations import create_db

def setup_database(app):
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/test.db"
    db.init_app(app)
    
def setup_blueprints(app):
    app.register_blueprint(mod_user, url_prefix = "")
    app.register_blueprint(mod_category, url_prefix = "")

def create_app():
    app = Flask(__name__)
    setup_database(app)
    setup_blueprints(app)
    return app

if __name__ == "__main__":
    app = create_app()
    create_db(app, db)
    app.run()