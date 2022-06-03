from app import db

class GenderBaju(db.Model):
    id_gender = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    nama_gender = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return '<Gender {}>'.format(self.id_gender)