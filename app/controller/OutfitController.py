from app.model.outfit import Outfit
from app import response,app,db
from flask import request

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