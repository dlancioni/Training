from src.models.category import Category

def get_categories(db):
    rs = Category.query.order_by(Category.name).all()
    return rs