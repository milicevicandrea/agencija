from app import db


class ChangeRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    wanted_account_type = db.Column(db.String(80))
    changed = db.Column(db.DateTime)
    admin = db.Column(db.Integer, db.ForeignKey('user.id'))
    # TODO dodaj datetime kad i ko je promenio account type - done

    def __init__(self, user_id, wanted_account_type, changed=None, admin=None):
        self.user_id = user_id
        self.wanted_account_type = wanted_account_type
        self.changed = changed
        self.admin = admin

    def __repr__(self):
        return '<User %r>' % self.id
