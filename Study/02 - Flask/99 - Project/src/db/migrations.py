import os
import shutil
from src.db.config import sqlite_path
from src.models.user import User
from src.models.category import Category
from src.models.product import Product
from src.models.product_info import ProductInfo

def create_db(app, db):
    with app.app_context():
        if not os.path.isfile(sqlite_path):
            db.drop_all()
            db.create_all()
            db.session.add(User("David"))
            db.session.add(User("Renata"))           
            db.session.add(Category("Açougue"))
            db.session.add(Category("Bebidas"))
            db.session.add(Category("Laticínios"))
            db.session.add(Category("Limpeza"))
            db.session.add(Category("Mercearia"))
            db.session.add(Product(2, "Cerveja Lager Premium Puro Malte Heineken Lata 350ml", "Cerveja Lager Premium Puro Malte Heineken, gelada, fresca e de alta qualidade. Apreciada em todos os lugares desde 1873.", 100, 4.39, 0))
            db.session.add(Product(2, "Cerveja Pilsen Antarctica Original Lata 350ml", "Cerveja Pilsen Antarctica Original, harmonize suas comemorações com um sabor mais suave e refrescante!", 100, 3.49, 0))
            db.session.add(ProductInfo(1, "Observação", "A venda e o consumo de bebidas alcoólicas são proibidos para menores de 18 anos. Beba com moderação. Se for dirigir, não beba!"))
            db.session.add(ProductInfo(1, "País de Origem", "Brasil"))
            db.session.add(ProductInfo(1, "Embalagem", "Lata"))
            db.session.add(ProductInfo(1, "Quantidade na Embalagem", "350 ml"))            
            db.session.commit()
    