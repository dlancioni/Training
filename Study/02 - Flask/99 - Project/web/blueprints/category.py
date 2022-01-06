from flask import Flask, render_template
from flask.blueprints import Blueprint
from src.models.category import Category

category = Blueprint("category", __name__, template_folder = "../templates", static_folder="static")

@category.route("/category_list")
def category_list():
  category = Category.query.filter_by(name="Food").first()
  return render_template("category.html", category=category)