import yaml
# config.yml is not in version control. Make a version based on sample_config.yml
f = open('app/config.yml')
configs = yaml.safe_load(f)
f.close()

class Config:
    # MySQL configurations
    user = configs['MYSQL_DATABASE_USER']
    password = configs['MYSQL_DATABASE_PASSWORD']
    db_name = configs['MYSQL_DATABASE_DB']
    db_host = configs['MYSQL_DATABASE_HOST']
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
        user, password, db_host, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
