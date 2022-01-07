from src.models.product import Product
from src.models.product_info import ProductInfo

def get_products(db):
    rs = db.session.query(Product).all()      
    return rs    