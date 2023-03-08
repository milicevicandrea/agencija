from app import db
from .destination import Destination
from .change_roles import ChangeRoles
from .reservation import Reservation


class User(db.Model):
    public_id = db.Column(db.String(80))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100))
    # password_again = db.Column(db.String(100))  # TODO izbaci - done
    account_type = db.Column(db.Integer, db.ForeignKey('account_type.id'))

    destinations = db.relationship('Destination', backref = 'guide_rel', foreign_keys=[Destination.guide])
    destinations1 = db.relationship('Destination', backref = 'created_by_rel', foreign_keys=[Destination.created_by])
    change_roles = db.relationship('ChangeRoles', backref = 'user_rel', foreign_keys = [ChangeRoles.user_id])
    change_roles1 = db.relationship('ChangeRoles', backref = 'admin_rel', foreign_keys = [ChangeRoles.admin])
    reservation = db.relationship('Reservation', backref='reserved_by_rel', foreign_keys = [Reservation.reserved_by])

    def __init__(self,  name, surname, email, username, account_type, password, public_id=None):
        self.public_id = public_id
        self.name = name
        self.surname = surname
        self.email = email
        self.username = username
        self.password = password
        # self.password_again = password_again
        self.account_type = account_type

    def __repr__(self):
        return '<User %r>' % self.username


