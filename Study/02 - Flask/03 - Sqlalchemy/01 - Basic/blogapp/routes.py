from blogapp import app
from blogapp.models import User, Post
from flask import render_template, url_for, flash, redirect

@app.route("/")
def home():
    user = User.query.get(1)
    return f"bem vindo ao blogapp {user.username}"