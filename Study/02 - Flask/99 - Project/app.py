import os.path
from flask import Flask
from database import db
# Models
from model import User
# Blueprints
from route_people import people

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    db.init_app(app)
    app.register_blueprint(people, url_prefix='')
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
    os.remove("test.db")
    if not os.path.isfile('/test.db'):
        setup_database(app)
    app.run()