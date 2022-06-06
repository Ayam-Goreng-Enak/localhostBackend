import imp
from app import app
from app import db
from app.controller import UserController
from app.controller import OutfitController


@app.route('/')
def testdb():
        return 'Hello World!'

@app.route('/allUser', methods=['GET'])
def allUser():
    return UserController.index()

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

@app.route('/register', methods=['POST'])
def register():
    return UserController.register()

@app.route('/allOutfit', methods=['GET'])
def allOutfit():
    return OutfitController.index()

@app.route('/addOutfit', methods=['POST'])
def addOutfit():
    return OutfitController.addOutfit()

@app.route('/getOutfit', methods=['POST'])
def getOutfit():
    return UserController.getOutfit()

@app.route('/recommend', methods=['POST'])
def recommend():
    return OutfitController.recommend()
