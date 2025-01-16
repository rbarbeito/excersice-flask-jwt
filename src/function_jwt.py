from jwt import encode, decode, exceptions
from os import getenv
from flask import jsonify
from datetime import datetime, timezone, timedelta


def write_token(data: dict):
    token = encode({**data, 'exp': datetime.now(tz=timezone.utc) +
                   timedelta(seconds=15)}, key=getenv('SECRET'), algorithm='HS256')
    return token.encode('utf-8')


def validate_token(token, output=False):

    try:
        if output:
            return decode(token, getenv('SECRET'), algorithms=['HS256'])

        decode(token, getenv('SECRET'), algorithms=['HS256'])

    except exceptions.DecodeError as e:
        response = jsonify({"msg": "Invalid Token"})
        response.status_code = 401

        return response

    except exceptions.ExpiredSignatureError as e:
        response = jsonify({"msg": "Token Expired"})
        response.status_code = 401
