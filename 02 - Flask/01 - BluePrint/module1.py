from flask import Blueprint, render_template, session,abort

module1 = Blueprint('module1',__name__)
@module1.route("/module1")
def fn():
    return "Hello World from module 1!"