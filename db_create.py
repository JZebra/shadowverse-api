#!flask/bin/python
from app import db
from app.models.card import Card
import os.path

json_url = 'sv.bagoum.com/cardsFullJSON'

# db.create_all()

# def create_faction():

# # test = Card("test card")
# # attrs = {'key1': 'val1', 'key2': 'val2'}
# # test.set_attrs(**attrs)
# db.session.add(test)
# db.session.commit()