from flask import Blueprint, request, jsonify
from function_jwt import write_token, validate_token


routes_auth = Blueprint('ruotes_auth', __name__)


@routes_auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if data['username'] == 'Bender' and data['password'] == 'bender':
        data['id'] = 7
        return write_token(data)
    else:
        response = jsonify({'msg': 'User and/or incorrect passwords'})
        response.status_code = 404

        return response


@routes_auth.route('/verify/token')
def verify_token():
    token = request.headers['Authorization'].split(' ')[1]
    response = validate_token(token, output=True)

    if response == No

    return ''
