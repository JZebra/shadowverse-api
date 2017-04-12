from app import db


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    cards = db.relationship('Card', backref='type')

    def __init__(self, name, **kwargs):
        self.name = name

    def __repr__(self):
        return '<Type {0}'.format(self.name)
