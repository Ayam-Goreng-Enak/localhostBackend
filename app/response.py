from flask import jsonify
from flask import make_response
from flask import request

def success(values,message='success'):
    res = {
        'data' : values,
        'message' : message
    }
    return make_response(jsonify(res), 200)

def badRequest(values,message='success'):
    res = {
        'data' : values,
        'message' : message
    }
    return make_response(jsonify(res), 400)