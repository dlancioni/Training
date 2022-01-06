from flask import Flask, render_template, sessions
from flask.blueprints import Blueprint
from src.models.category import Category
from db.config import db

store = Blueprint("store", __name__, template_folder = "../templates", static_folder="static")

@store.route("/")
def home():
    #category = Category.query.filter().order_by("name")
    category = db.session.query(Category)
    return render_template("store.html", category=category)
