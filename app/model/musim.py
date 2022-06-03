from app import db

class Musim(db.Model):
    id_musim = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    nama_musim = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Musim {}>'.format(self.nama_musim)