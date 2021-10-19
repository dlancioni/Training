from flask import Flask
from database import database

# blueprint import
from apps.app1.views import app1

def create_app():

    # new instance
    app = Flask(__name__)

    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    
    # setup all our dependencies
    database.init_app(app)
    
    # register blueprint
    app.register_blueprint(app1, url_prefix="/app1")
    
    # done
    return app

if __name__ == "__main__":
    create_app().run()