from app import app
from ..views import posts, helper

"""Neste arquivo iremos criar todas rotas para aplicação para manter o código limpo usando
 as views(controllers)  e as relacionando por meio de funções"""


@app.route('/v1/posts', methods=['GET'])
@helper.token_required
def get_posts(current_user):
    return posts.get_posts(current_user)


@app.route('/v1/posts/<id>', methods=['GET'])
@helper.token_required
def get_post(current_user, id):
    return posts.get_post(current_user, id)


@app.route('/v1/posts', methods=['POST'])
@helper.token_required
def post_posts(current_user):
    return posts.post_post(current_user)


@app.route('/v1/posts/<id>', methods=['DELETE'])
@helper.token_required
def delete_posts(current_user, id):
    return posts.delete_post(current_user, id)


@app.route('/v1/posts/<id>', methods=['PUT'])
@helper.token_required
def update_posts(current_user, id):
    return posts.update_post(current_user, id)

