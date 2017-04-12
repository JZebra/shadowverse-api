from app import db


class Expansion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    cards = db.relationship('Card', backref='expansion')

    def __init__(self, name, **kwargs):
        self.name = name

    def __repr__(self):
        return '<Expansion {0}'.format(self.name)
