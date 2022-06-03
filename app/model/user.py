from app import db
from datetime import datetime
from sqlalchemy.orm import backref

class User(db.Model):
    id_user = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_role = db.Column(db.BIGINT, db.ForeignKey("role.id_role"), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    lokasi = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),index=True,unique=True, nullable=False)
    no_hp = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(25),unique=True, nullable=False)
    photo = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)


    user_role = db.relationship("Role", backref=backref("User", uselist=False))# one to one relationship
    # def __repr__(self) -> str:
    #     return super().__repr__()
    def __repr__(self):
        return '<User {}>'.format(self.nama)
