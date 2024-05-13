from flask import Flask, render_template
from flask.blueprints import Blueprint
from src.controller import user as UserController

bp_user = Blueprint("user", __name__)

@bp_user.route("/save")
def user_list():
    userController = UserController()
    userController.save()
    return render_template("user.html")