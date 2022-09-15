from app import app
from flask import jsonify
from ..views import users, helper

"""Neste arquivo iremos criar todas rotas para aplicação para manter o código limpo usando
 as views(controllers)  e as relacionando por meio de funções"""


@app.route('/v1', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify({'message': f'Hello {current_user.name}'})


@app.route('/v1/authenticate', methods=['POST'])
def authenticate():
    return helper.auth()


@app.route('/v1/users', methods=['GET'])
@helper.token_required
def get_users(current_user):
    return users.get_users(current_user)


@app.route('/v1/users/<id>', methods=['GET'])
@helper.token_required
def get_user(current_user, id):
    return users.get_user(current_user, id)


@app.route('/v1/users', methods=['POST'])
def post_users():
    return users.post_user()


@app.route('/v1/users/<id>', methods=['DELETE'])
def delete_users(current_user, id):
    return users.delete_user(current_user, id)


@app.route('/v1/users/<id>', methods=['PUT'])
@helper.token_required
def update_users(current_user, id):
    return users.update_user(current_user, id)


@app.route('/v1/auth', methods=['POST'])
@helper.token_required
def auth():
    pass
