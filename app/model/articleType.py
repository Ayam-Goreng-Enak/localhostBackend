from app import db

class ArticleType(db.Model):
    id_tipe = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_sub_category = db.Column(db.BIGINT, db.ForeignKey("sub_category.id_sub_category"), nullable=False)
    nama_tipe = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return '<ArticleType {}>'.format(self.nama_tipe)