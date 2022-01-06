import os.path
from src.models.user import User
from src.models.category import Category
from src.models.product import Product

def create_db(app, db):
    with app.app_context():
        if not os.path.isfile("db/db.dat"):
            try:
                db.create_all()
                db.session.add(User("David"))
                db.session.add(User("Renata"))
                
                db.session.add(Category("Bebidas"))
                db.session.add(Category("Padaria"))
                
                db.session.add(Product(1, "Heineken", "Cerveja pilsen 600 ml", 100, 8.00, 0))
                db.session.add(Product(1, "Original", "Cerveja pilsen 600 ml", 100, 6.00, 0))
                
                db.session.commit()                
            except:
                pass

                

    