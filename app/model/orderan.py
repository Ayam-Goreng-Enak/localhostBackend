from app import db


class Orderan(db.Model):
    id_orderan = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BIGINT, db.ForeignKey("user.id_user"), nullable=False)
    payment = db.Column(db.Integer, nullable=True)
    total = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Orderan {}>'.format(self.id_orderan)