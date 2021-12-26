# https://flask-admin.readthedocs.io/en/v1.0.8/quickstart/
# https://github.com/mrjoes/flask-admin/blob/master/examples/sqla/app.py
# https://github.com/mrjoes/flask-admin/tree/master/examples/sqla
   
from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib import sqla
from flask_admin import Admin, BaseView, expose
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

# create app
app = Flask(__name__)
app.config["SECRET_KEY"] = "0123456789"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

# User
class UserCust(sqla.ModelView):
    column_display_pk = True
    form_columns = ["id", "username", "email"]    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    def __str__(self):
        return self.username
    
# Post    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)    

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='microblog', template_mode='bootstrap3')

# addview (screens)
admin.add_view(ModelView(User, db.session, category='Entry'))
admin.add_view(ModelView(Post, db.session, category='Entry'))
admin.add_view(MyView(name='Other', endpoint='endpoint', category='Entry'))

if __name__ == '__main__':
   app.run(debug=True)