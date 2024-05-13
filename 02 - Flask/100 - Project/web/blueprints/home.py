from flask import render_template
from flask.blueprints import Blueprint
from src.models.user import User

home = Blueprint("home", __name__, template_folder = "../templates", static_folder="static")
@home.route("/")
def main():
    
    users = User.query.all()
    users = [user.username for user in users]
    
    return render_template("home.html")
