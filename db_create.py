#!flask/bin/python
# from migrate.versioning import api
from app import db
from app.models.card import Card
import os.path

db.create_all()
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#     api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
#     api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

test = Card("test card")
attrs = {'key1': 'val1', 'key2': 'val2'}
test.set_attrs(**attrs)
db.session.add(test)
db.session.commit()