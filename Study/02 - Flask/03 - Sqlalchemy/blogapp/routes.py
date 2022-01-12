from blogapp import app
from blogapp.models import db, User, Post
from flask import render_template, url_for, flash, redirect

@app.route("/")
def home():
    user = User.query.get(1)
    return f"bem vindo ao blogapp {user.username}"

@app.route("/query1")
def query1():
    user = db.session.query(User).filter(User.id == 2).all()
    return f"bem vindo ao blogapp {(user)}"

@app.route("/query2")
def query2():
    where = User.id == 1
    where += User.id == 2
    user = db.session.query(User).filter(where).all()
    return f"bem vindo ao blogapp {(user)}"