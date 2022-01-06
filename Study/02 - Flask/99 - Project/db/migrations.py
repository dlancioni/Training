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
                db.session.add(Category("Padaria"))
                db.session.add(Category("Açougue"))
                db.session.add(Category("Limpeza"))
                db.session.add(Category("Laticineos"))
                db.session.add(Category("Frutas"))
                db.session.add(Category("Verduras"))
                db.session.add(Category("Bebidas"))
                db.session.commit()                
            except:
                db.rollback()
                

    