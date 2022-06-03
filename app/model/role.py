from app import db
from datetime import datetime

class Role(db.Model):
    id_role = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    nama_role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.nama_role)