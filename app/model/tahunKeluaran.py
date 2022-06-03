from app import db

class TahunKeluaran(db.Model):
    id_tahun = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    tahun = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Tahun {}>'.format(self.id_tahun)