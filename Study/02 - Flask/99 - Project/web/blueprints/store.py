from flask import Flask, render_template
from flask.blueprints import Blueprint

store = Blueprint("store", __name__, template_folder = "../templates", static_folder="static")

@store.route("/")
def home():   
    return render_template("store.html")
