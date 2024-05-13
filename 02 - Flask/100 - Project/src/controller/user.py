from src.db.config import db
from src.models.user import User as UserModel

class User():

    def __init__(self):
        pass

    def save(self, model):
        db.session.add(model)
        db.session.commit()
        UserModel.query.filter_by(role='admin').update()
    
    def list(self):
        rs = UserModel.query.order_by(UserModel.id).all()
        return rs
