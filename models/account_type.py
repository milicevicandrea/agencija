from app import db
from models import User


class AccountType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(30))

    users = db.relationship('User', backref='account_type_rel', foreign_keys=[User.account_type])

    def __init__(self, account_type):
        self.account_type = account_type

    def __rep__(self):
        return '<Account type %r>' % self.username
