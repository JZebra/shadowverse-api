from flask import Flask, jsonify, render_template
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
import jsonpickle
import yaml

from config import Config
from models import card

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

mysql = MySQL()

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/dev/')
def get_all():
    return jsonpickle.encode({'cards': card.Card.query.all()})


@app.route('/cards/named')
def get_card():
    pass


# @app.route('/sets')
# def get_set():
#     TODO


# @app.route('/class')
# def get_class():
#     TODO


if __name__ == '__main__':
    #init db
    mysql.init_app(app)
    app.run(debug=True)
