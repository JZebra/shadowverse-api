from flask import Flask, render_template
from flaskext.mysql import MySQL
import yaml

app = Flask(__name__)
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

@app.route('/')
def main():
    return render_template('index.html')


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
