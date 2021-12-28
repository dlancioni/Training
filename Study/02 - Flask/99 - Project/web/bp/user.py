from flask import Flask, render_template
from flask.blueprints import Blueprint
from src.models.user import User

bp_user = Blueprint('bp_user', __name__, template_folder = "../templates", static_folder="static")

@bp_user.route('/user_list')
def user_list():

    try:
        users = User.query.all()
        users = [user.username for user in users]
    except Exception:
        users = "Something went wrong"
      
    return render_template('user.html', users=users)
