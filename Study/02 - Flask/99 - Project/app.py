import os.path
from flask import Flask
from models.user import User
from modules.user import mod_user
from db.config import db

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/test.db"
    db.init_app(app)
    app.register_blueprint(mod_user, url_prefix='')
    return app 

def setup_database(app):
    with app.app_context():
        db.create_all()
        user = User()
        user.username = "Tom"
        db.session.add(user)
        db.session.commit()    

if __name__ == '__main__':
    app = create_app()
    if not os.path.isfile('db/test.db'):
        setup_database(app)
    app.run()