from app import db

class JenisOutfit(db.Model):
    id_jenis = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    nama_jenis = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Jenis {}>'.format(self.nama_jenis)