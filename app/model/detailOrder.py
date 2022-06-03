from app import db


class DetailOrder(db.Model):
    id_detail = db.Column(db.BIGINT, primary_key=True, autoincrement=True, nullable=False)
    id_orderan = db.Column(db.BIGINT, db.ForeignKey("orderan.id_orderan"), nullable=False)
    id_user = db.Column(db.BIGINT, db.ForeignKey("user.id_user"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    harga_item = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<DetailOrder {}>'.format(self.id_detail)