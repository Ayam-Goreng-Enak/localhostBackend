from app import db

class Style(db.Model):
    id_style = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    nama_style = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return '<Style {}>'.format(self.nama_style)