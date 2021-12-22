# https://flask.palletsprojects.com/en/2.0.x/config/
import os
import json
from flask import Flask
from module1 import module1
from configparser import ConfigParser

app = Flask(__name__)
app.register_blueprint(module1)

# environment variable
# Set in powershell: $env:APP_ENV="production"
# use this approach to define which configuration file you will use
appenv = os.environ.get("APP_ENV")
if not appenv:
    raise ValueError("No APP_ENV set for Flask application")

# override configuration example
app.config.from_file("config.json", load=json.load)
print(app.secret_key)
print(app.env)

# ini example
file = "config.ini"
config = ConfigParser()
config.read(file)
print(config.sections())

upload_folder = config["upload"]["folder"]

servername = config["database"]["server"]
username = config["database"]["username"]
password = config["database"]["password"]

# start up app
if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)