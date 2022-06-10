from app import app
import sqlalchemy
from google.cloud.sql.connector import connector


def CloudSQL() -> sqlalchemy.engine.Engine:
    def getconn() -> connector.connect:
        conn = connector.connect(
            "caps-test-352212:asia-southeast1:capfitsdb", 
            "pymysql",
            user="root",
            password="123456",
            db="capfits_db")
        return conn

    engine = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    return engine