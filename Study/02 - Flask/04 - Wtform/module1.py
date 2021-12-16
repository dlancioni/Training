from flask import Blueprint, render_template, session, request
from forms import Form1, Form2

module1 = Blueprint('module1',__name__)

@module1.route('/form1', methods=('GET', 'POST'))
def form1():
    form = Form1()
    if form.validate_on_submit():
        return f"<h1> Welcome {form.firstname.data} {form.lastname.data} </h1>"
    return render_template('form1.html', form=form)

@module1.route('/form2', methods=('GET', 'POST'))
def form2():
    form = Form2()
    if form.validate_on_submit():
        return f"<h1> Authenticated {form.username.data} </h1>"
    return render_template('form2.html', form=form)