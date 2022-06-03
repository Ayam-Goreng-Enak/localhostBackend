from app import db

class Size(db.Model):
    id_size = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_outfit = db.Column(db.BIGINT, db.ForeignKey("outfit.id_outfit"), nullable=False)
    size = db.Column(db.String(16), nullable=False)
    waist = db.Column(db.String(6), nullable=False)
    hip = db.Column(db.String(6), nullable=False)
    length = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return '<Size {}>'.format(self.size)