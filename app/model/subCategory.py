from app import db

class SubCategory(db.Model):
    id_sub_category = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_master_category = db.Column(db.BIGINT, db.ForeignKey("master_category.id_master_category"), nullable=False)
    nama_sub_category = db.Column(db.String(50), nullable=False)
    
    type = db.relationship("ArticleType")
    def __repr__(self):
        return '<SubCategory {}>'.format(self.nama_sub_category)