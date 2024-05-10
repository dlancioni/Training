from flask import Blueprint

users = Blueprint('users', __name__)
@users.route("/users")
def fn():
    return "Hello World from module users!"