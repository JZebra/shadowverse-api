from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    faction = db.Column(db.Integer, index=True) #fk
    type = db.Column(db.Integer, index=True) #fk
    expansion = db.Column(db.Integer, index=True) #fk
    race = db.Column(db.Integer, index=True) #fk currently only used for traits
    hasEvo = db.Column(db.Boolean)
    rarity = db.Column(db.Integer, index=True) #fk
    game_id = db.Column(db.Integer)
    hasAlt = db.Column(db.Integer)
    manaCost = db.Column(db.Integer)
    baseData = db.Column(db.Integer)
    base_attack = db.Column(db.Integer)
    base_defense = db.Column(db.Integer)
    base_description = db.Column(db.Text)
    base_flair = db.Column(db.Text)
    base_img = db.Column(db.String(1024))
    evolved_attack = db.Column(db.Integer)
    evolved_defense = db.Column(db.Integer)
    evolved_description = db.Column(db.Text)
    evolved_flair = db.Column(db.Text)
    evolved_img = db.Column(db.String(1024))
    # TODO: figure out a better way to do this. sqlalchemy does not support full text
    # indexes on this storage engine
    searchableText = db.Column(db.Text)
    logo = db.Column(db.String(1024))

    def __init__(self, name, **kwargs):
        self.name = name

    def __repr__(self):
        return '<Card {0}'.format(self.name)

    def set_attrs(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
