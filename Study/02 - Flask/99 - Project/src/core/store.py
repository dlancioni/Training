from src.models.product import Product
from src.models.product_info import ProductInfo

def get_products(db):
    rs = db.session.query(Product, ProductInfo).join(ProductInfo).all()
    for product, productInfo in rs:
        x = product.name
        y = productInfo.key + " - " + productInfo.value
    return rs    