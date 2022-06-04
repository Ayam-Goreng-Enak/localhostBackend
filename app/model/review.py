from app import db

class Review(db.Model):
    id_review = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BIGINT, db.ForeignKey('user.id_user'))
    id_outfit = db.Column(db.BIGINT, db.ForeignKey("outfit.id_outfit"), nullable=False)
    ulasan = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    tanggal_review = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Review {}>'.format(self.ulasan)