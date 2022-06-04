from app.model.user import User
from app.model import role
from app import response,app,db
from flask import request
import json

def index():
    try:
        users = User.query.all()
        
        return response.success(formatArray(users),"success")
    except Exception as e:
        print(e)
        return response.badRequest(e)

def login():
    data = json.loads(request.data)
    try:
        email = data['email']
        password = data['password']
        print(email,password)
        user = User.query.filter_by(email=email,password=password).first()
        print(user)
        if user is None:
            return response.badRequest("Username or Password is wrong")
        return response.success(singleObject(user),"success")
    except Exception as e:
        return response.badRequest(e)

def register():
    try:
        id_role = request.json['id_role']
        nama = request.json['nama']
        lokasi = request.json['lokasi']
        email = request.json['email']
        no_hp = request.json['no_hp']
        password = request.json['password']
        username = request.json['username']
        photo = request.json['photo']
        user = User(id_role=id_role,nama=nama,lokasi=lokasi,email=email,no_hp=no_hp,password=password,username=username,photo=photo)
        db.session.add(user)
        db.session.commit()
        return response.success(singleObject(user),"success")
    except Exception as e:
        return response.badRequest(e)

        
def formatArray(data):
    arr = []

    for d in data:
        arr.append(singleObject(d))

    return arr

def singleObject(userData):
    userData = {
        'id_user': userData.id_user,
        'id_role': userData.id_role,
        'nama': userData.nama,
        'lokasi': userData.lokasi,
        'email': userData.email,
        'no_hp': userData.no_hp,
        'password': userData.password,
        'username': userData.username,
        'photo': userData.photo
    }
    return userData