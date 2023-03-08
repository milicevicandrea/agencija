from app import db


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'))
    price = db.Column(db.Integer)
    reserved_by = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, destination_id, price, reserved_by):
        self.destination_id = destination_id
        self.price = price
        self.reserved_by = reserved_by

    def __repr__(self):
        return '<User %r>' % self.id
