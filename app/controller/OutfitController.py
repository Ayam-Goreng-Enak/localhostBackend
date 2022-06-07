from pyexpat import model
from app.model.outfit import Outfit
from app.model.user import User
from app.model.foto_outfit import FotoOutfit
from app.model.review import Review
from MLmodel.recommender import recommend
import base64
import PIL.Image as Image
import io
import os
from app import response,app,db
from flask import request
import json
from sqlalchemy import text
from sqlalchemy import create_engine

def index():
    try:
        outfits = Outfit.query.all()
        
        return response.success(formatArray(outfits),"success")
    except Exception as e:
        print(e)
        return response.badRequest(e)


def getOutfit():
    try:
        id_outfit = request.json['id_outfit']
        outfit = Outfit.query.filter_by(id_outfit=id_outfit).first()
        if outfit is None:
            return response.badRequest("Outfit not found")
        return response.success(singleObject(outfit),"success")
    except Exception as e:
        return response.badRequest(e)

def addOutfit():
    try:
        id_user = request.json['id_user']
        id_kategori = request.json['id_kategori']
        id_gender = request.json['id_gender']
        id_jenis = request.json['id_jenis']
        id_tahun = request.json['id_tahun']
        id_musim = request.json['id_musim']
        id_tipe = request.json['id_tipe']
        warna = request.json['warna']
        nama_outfit = request.json['nama_outfit']  
        harga_sewa = request.json['harga_sewa']  
        harga_beli = request.json['harga_beli']
        ukuran = request.json['ukuran']    
        deskripsi = request.json['deskripsi']       
        detail_produk = request.json['detail_produk'],
        id_style = request.json['id_style']      
        is_keranjang = request.json['is_keranjang'],
        is_wishlish = request.json['is_wishlish']
        stock = request.json['stock']  
        outfit = Outfit(id_user,id_kategori,id_kategori,id_gender,id_jenis,id_tahun,id_tahun,
                        id_musim,id_tipe,warna,nama_outfit,harga_sewa,harga_beli,ukuran,deskripsi,detail_produk,id_style,is_keranjang,is_wishlish,stock)
        db.session.add(outfit)
        db.session.commit()
        return response.success(singleObject(outfit),"success")
    except Exception as e:
        return response.badRequest(e)

def decodeB64(data):
    image_64_decode = base64.b64decode(data) # base64.decode(image_64_encode)
    return image_64_decode

def rec():
    try:
        data = json.loads(request.data)
        bytearrimg = decodeB64(data)
        byteimg = bytearray(bytearrimg)
        img = Image.open(io.BytesIO(byteimg))
        img.save(os.getcwd()+'\MLmodel\img1.jpg')
        id_rec, index_sim = recommend(os.getcwd()+'\MLmodel\img1.jpg')
        recommended=[]
        # wanted to queried

        # SELECT outfit.`id_outfit`,foto_outfit.`foto`,nama_outfit,harga_sewa,lokasi,rating FROM outfit
        # JOIN USER ON user.`id_user` = outfit.`id_user`
        # JOIN foto_outfit ON foto_outfit.`id_outfit` = outfit.`id_outfit`
        # LEFT JOIN review ON review.`id_outfit` = outfit.`id_outfit`
        # WHERE outfit.`id_outfit` = 1636
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + str(os.environ.get('DB_USERNAME')) + ':' + str(os.environ.get('DB_PASS')) + '@' + str(os.environ.get('DB_HOST')) + '/' + str(os.environ.get('DB_DATABASE'))
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        
        with engine.connect() as connection:
            for id in id_rec:
                result = connection.execute(text("SELECT outfit.`id_outfit`,foto_outfit.`foto`,nama_outfit,harga_sewa,lokasi,rating FROM outfit JOIN USER ON user.`id_user` = outfit.`id_user` JOIN foto_outfit ON foto_outfit.`id_outfit` = outfit.`id_outfit` LEFT JOIN review ON review.`id_outfit` = outfit.`id_outfit` WHERE outfit.`id_outfit` = {}".format(id)))
                for row in result:
                    recommended.append(row)
        print(recommended)
        # for id in id_rec:
        #     recommended.append(Outfit.query.all().join(User, User.id_user == Outfit.id_user).join(FotoOutfit, FotoOutfit.id_outfit == Outfit.id_outfit).join(Review, Review.id_outfit == Outfit.id_outfit,isouter = True).filter(Outfit.id_outfit == id).all())
        # query = session.query(User, Document, DocumentsPermissions).join(Document).join(DocumentsPermissions)
        return response.success(formatArrayRec(recommended),"success")
    except Exception as e:
        return response.badRequest(e)

def formatArrayRec(data):
    arr = []

    for d in data:
        arr.append(singleObjectRec(d))

    return arr

def singleObjectRec(data):
    data = {
        'id_outfit': data.id_outfit,
        'foto': data.foto,
        'nama_outfit': data.nama_outfit,
        'harga_sewa': data.harga_sewa,
        'lokasi': data.lokasi,
        'rating': data.rating
    }
    return data

def formatArray(data):
    arr = []

    for d in data:
        arr.append(singleObject(d))

    return arr

def singleObject(outfitData):
    outfitData = {
        'id_outfit': outfitData.id_outfit,
        'id_user': outfitData.id_user,
        'id_kategori': outfitData.id_kategori,
        'id_gender': outfitData.id_gender,
        'id_jenis': outfitData.id_jenis,
        'id_tahun': outfitData.id_tahun,
        'id_musim': outfitData.id_musim,
        'id_tipe': outfitData.id_tipe,
        'warna': outfitData.warna,
        'nama_outfit': outfitData.nama_outfit,
        'harga_sewa': outfitData.harga_sewa,
        'harga_beli': outfitData.harga_beli,
        'ukuran': outfitData.ukuran,
        'deskripsi': outfitData.deskripsi,
        'detail_produk': outfitData.detail_produk,
        'id_style': outfitData.id_style,
        'is_keranjang': outfitData.is_keranjang,
        'is_wishlish': outfitData.is_wishlish,
        'stock': outfitData.stock
    }
    return outfitData