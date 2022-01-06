from flask import Flask, render_template
from flask.blueprints import Blueprint

bp_home = Blueprint('bp_home', __name__, template_folder = "../templates", static_folder="static")

@bp_home.route('/')
def home():   
    return render_template('home.html')
