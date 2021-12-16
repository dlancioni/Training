from flask import Blueprint, render_template, session, request
from forms import Form1

module1 = Blueprint('module1',__name__)


@module1.route('/', methods=('GET', 'POST'))
def index():
    form = Form1()
    if form.validate_on_submit():
        return f'''<h1> Welcome {form.username.data} </h1>'''
    return render_template('form1.html', form=form)