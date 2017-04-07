from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL
import yaml

app = Flask(__name__)
api = Api(app)
mysql = MySQL()

# config.yml is not in version control. Make a version based on sample_config.yml
f = open('./config.yml')
configs = yaml.safe_load(f)
f.close()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = configs['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = configs['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = configs['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST'] = configs['MYSQL_DATABASE_HOST']

# sample from tutorial
# class CreateUser(Resource):
#     def post(self):
#         try:
#             # Parse the arguments
#             parser = reqparse.RequestParser()
#             parser.add_argument('email', type=str, help='Email address to create user')
#             parser.add_argument('password', type=str, help='Password to create user')
#             args = parser.parse_args()

#             _userEmail = args['email']
#             _userPassword = args['password']

#             #persist to db
#             conn = mysql.connect()
#             cursor = conn.cursor()
#             cursor.callproc('spCreateUser',(_userEmail,_userPassword))
#             data = cursor.fetchall()
#             if len(data) is 0:
#                conn.commit()
#                return {'StatusCode':'200','Message': 'User creation success'}
#             else:
#                return {'StatusCode':'1000','Message': str(data[0])}

#         except Exception as e:
#             return {'error': str(e)}


if __name__ == '__main__':
    #init db
    mysql.init_app(app)
    app.run(debug=True)
