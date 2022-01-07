from flask import Flask, render_template, sessions
from flask.blueprints import Blueprint
from src.models.category import Category
from src.db.config import db
from src.core.store import get_products
from src.core.category import get_categories


store = Blueprint("store", __name__, template_folder = "../templates", static_folder="static")

@store.route("/")
def home():
    #category = Category.query.order_by(Category.name).all()
    rs1 = get_categories(db)
    rs2 = get_products(db)
    
    return render_template("store.html", category=rs1)
