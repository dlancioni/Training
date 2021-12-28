import os.path
from src.models.user import User
from src.models.category import Category

def create_db(app, db):
    with app.app_context():
        if not os.path.isfile("db/db.dat"):
            try:
                db.create_all()
                db.session.add(User("David"))
                db.session.add(User("Renata"))
                db.session.add(User("Taza"))
                db.session.add(Category("Home"))
                db.session.add(Category("Auto"))
                db.session.add(Category("Food"))
                db.session.commit()                
            except:
                db.rollback()
                

    