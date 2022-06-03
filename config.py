import os

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get('DB_HOST'))
    DATABASE = str(os.environ.get('DB_DATABASE'))
    USERNAME = str(os.environ.get('DB_USERNAME'))
    PASSWORD = str(os.environ.get('DB_PASS'))

    #localhost
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE

    # # configuration Google Cloud SQL (change this accordingly)
    # PASSWORD ="123456"
    # PUBLIC_IP_ADDRESS ="public ip of database"
    # DBNAME ="capfits"
    # PROJECT_ID ="gcp project id"
    # INSTANCE_NAME ="capfits-c22-ps041:asia-southeast2:db-capfits"
    # # GCP
    # SECRET_KEY = "yoursecretkey"
    # SQLALCHEMY_DATABASE_URI = f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
    

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    

