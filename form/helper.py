from form import app
from functools import wraps
from flask import request, jsonify
import jwt, datetime


def auth():
    token = jwt.encode(
        {'name': 'adm', 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                           app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'message': 'Validated successfully', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(data, *args, **kwargs)
    return decorated