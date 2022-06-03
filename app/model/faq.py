from app import db

class Faq(db.Model):
    id_faq = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(50), nullable=False)
    deskripsi = db.Column(db.String(500), nullable=False)
    foto = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Faq {}>'.format(self.judul)