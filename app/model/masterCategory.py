from app import db

class MasterCategory(db.Model):
    id_master_category = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    nama_master = db.Column(db.String(50), nullable=False)

    sub = db.relationship("SubCategory")
    def __repr__(self):
        return '<MasterCategory {}>'.format(self.nama_master)