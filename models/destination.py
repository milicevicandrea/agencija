from app import db
from .reservation import Reservation


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starts = db.Column(db.Date)
    ends = db.Column(db.Date)
    description = db.Column(db.String(500))
    destination = db.Column(db.String(40))
    number_of_people = db.Column(db.Integer)
    price = db.Column(db.Integer)
    guide = db.Column(db.Integer, db.ForeignKey('user.id'))  # TODO guide_id i created_by_id, relacije koje se tako zovu - promenjeno u guide_rel
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))

    reservation = db.relationship('Reservation', backref='destination_rel', foreign_keys=[Reservation.destination_id])

    def __init__(self, starts, ends, description, destination, number_of_people, price, guide=None, created_by=None):
        self.starts = starts
        self.ends = ends
        self.description = description
        self.destination = destination
        self.number_of_people = number_of_people
        self.price = price
        self.guide = guide
        self.created_by = created_by

    def __repr__(self):
        return '<Destination %r>' % self.destination