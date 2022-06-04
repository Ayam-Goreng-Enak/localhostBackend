from app import db
import enum
from sqlalchemy import Enum

class Outfit(db.Model):
    id_outfit = db.Column(db.BIGINT, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BIGINT, db.ForeignKey("user.id_user"), nullable=False)
    id_kategori = db.Column(db.BIGINT, db.ForeignKey("kategori.id_kategori"), nullable=False)
    id_gender = db.Column(db.BIGINT, db.ForeignKey("gender_baju.id_gender"), nullable=True)
    id_jenis = db.Column(db.BIGINT, db.ForeignKey("jenis_outfit.id_jenis"), nullable=True)
    id_tahun = db.Column(db.BIGINT, db.ForeignKey("tahun_keluaran.id_tahun"), nullable=True)
    id_musim = db.Column(db.BIGINT, db.ForeignKey("musim.id_musim"), nullable=True)
    id_tipe = db.Column(db.BIGINT, db.ForeignKey("article_type.id_tipe"), nullable=True)
    warna = db.Column(db.String(100), nullable=False)
    nama_outfit = db.Column(db.String(100), nullable=False)
    harga_sewa = db.Column(db.Integer, nullable=False)
    harga_beli = db.Column(db.Integer, nullable=False)
    ukuran = db.Column(db.String(20), nullable=False)
    deskripsi = db.Column(db.String(500), nullable=False)
    detail_produk = db.Column(db.String(300), nullable=False)
    id_style = db.Column(db.BIGINT, db.ForeignKey("style.id_style"), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Outfit {}>'.format(self.nama_outfit)