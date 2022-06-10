import os
from google.cloud.sql.connector import connector
import sqlalchemy
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # HOST = str(os.environ.get('DB_HOST'))
    # DATABASE = str(os.environ.get('DB_DATABASE'))
    # USERNAME = str(os.environ.get('DB_USERNAME'))
    # PASSWORD = str(os.environ.get('DB_PASS'))

    # # localhost
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE

    # configuration Google Cloud SQL (change this accordingly)
    # PASSWORD ="123456"
    # HOST ="34.142.214.10"
    # USERNAME = str(os.environ.get('DB_USERNAME'))
    # DATABASE ="capfits_db"
    # PROJECT_ID ="caps-test-352212"
    # INSTANCE_NAME = "caps-test-352212:asia-southeast1:capfitsdb"
    # INSTANCE_ZONE = "asia-southeast1-b"

    # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE+"?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_ZONE}:{INSTANCE_NAME}"
    

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    

