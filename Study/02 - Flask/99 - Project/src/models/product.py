from db.config import db

class Product(db.Model):
    
    def __init__(self, category, name, description, amount, price, discount):
        self.category = category
        self.name = name
        self.description = description
        self.amount = amount
        self.price = price
        self.discount = discount
        
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)    
    name = db.Column(db.String(50), unique = True)
    description = db.Column(db.Text, unique = False)
    amount = db.Column(db.Float, unique = False)
    price = db.Column(db.Float, unique = False)
    discount = db.Column(db.Float, unique = False)

    
    def __str__(self):
        return f"Product: Category {self.category}, Name {self.name}, Description {self.description}, Amount {self.amount}, Price {self.price}, Discount {self.discount}"


