from flask import Blueprint, render_template, session,abort

logdemo = Blueprint('logdemo',__name__)
@logdemo.route("/")
@logdemo.route("/logdemo")
def fn():
    logdemo.logger.info("My first log info")
    return "Hello World from module 1!"