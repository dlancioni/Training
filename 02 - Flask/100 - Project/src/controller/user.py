from src.db.config import db
from src.models.user import User as UserModel

class Users():

    def __init__(self, db):
        self.db = db

    def save(self):
        db.session.add(Users("User 99"))
        db.session.commit()
    
    def query(self):
        rs = UserModel.query.order_by(UserModel.name).all()
        return rs
