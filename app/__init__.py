from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.model import masterCategory
from app.model import subCategory
from app.model import articleType
from app.model import role
from app.model import user
from app.model import kategori
from app.model import tahunKeluaran
from app.model import style
from app.model import genderBaju
from app.model import musim
from app.model import outfit
from app.model import size
from app.model import foto_outfit

from app.model import detailOrder
from app.model import faq
from app.model import orderan
from app.model import review

