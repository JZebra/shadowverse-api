from app import db


class Trait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    cards = db.relationship('Card', backref='trait')

    def __init__(self, name, **kwargs):
        self.name = name

    def __repr__(self):
        return '<Trait {0}'.format(self.name)
