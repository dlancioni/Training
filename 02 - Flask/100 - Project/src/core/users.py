from src.models.user import User as user

class User():

    def __init__(self, db):
        self.db = db

    def get_category(self):
        rs = user.query.order_by(user.name).all()
        return rs