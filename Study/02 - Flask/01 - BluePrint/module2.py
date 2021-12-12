from flask import Blueprint, render_template, session,abort

module2 = Blueprint('module2',__name__)
@module2.route("/module2")
def fn():
    return "Hello World from module2!"