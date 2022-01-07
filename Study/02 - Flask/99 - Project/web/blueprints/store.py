from flask import Flask, render_template
from flask.blueprints import Blueprint
from src.db.config import db

from src.core.product import Product
from src.core.category import Category


store = Blueprint("store", __name__, template_folder = "../templates", static_folder="static")

@store.route("/")
def home():
    
    product = Product(db)
    category = Category(db)
    
    rs1 = category.get_category()
    rs2 = product.get_product()
    
    return render_template("store.html", category=rs1, product=rs2)
