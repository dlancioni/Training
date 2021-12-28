import os.path
from models.user import User
from models.category import Category

def create_db(app, db):
    with app.app_context():
        if not os.path.isfile("db/test.db"):
            # create tables
            db.create_all()
            # Users    
            user = User()
            user.username = "Tom"
            db.session.add(user)        
            # Categories
            category = Category()
            category.name = "Food"
            db.session.add(category)
            # all good
            db.session.commit()
    