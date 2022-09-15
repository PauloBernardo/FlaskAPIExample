from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.posts import Posts, post_schema, posts_schema


"""Retorna lista de usuários"""


def get_posts(current_user):
    name = request.args.get('name')
    if name:
        posts = Posts.query.filter(Posts.name.like(f'%{name}%')).all()
    else:
        posts = Posts.query.all()
    if posts:
        result = posts_schema.dump(posts)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'nothing found', 'data': {}})


"""Retorna usuário específico pelo ID no parametro da request"""


def get_post(current_user, id):
    post = Posts.query.get(id)
    if post:
        result = post_schema.dump(post)
        return jsonify({'message': 'successfully fetched', 'data': result.data}), 201

    return jsonify({'message': "post don't exist", 'data': {}}), 404


"""Cadastro de usuários com validação de existência"""


def post_post(current_user):
    title = request.json['title']
    description = request.json['description']
    user_id = current_user.id

    post = Posts(title, description, user_id)

    try:
        db.session.add(post)
        db.session.commit()
        result = post_schema.dump(post)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': 'unable to create', 'data': {}}), 500


"""Atualiza usuário baseado no ID, caso o mesmo exista."""


def update_post(current_user, id):
    description = request.json.get('description', None)
    title = request.json.get('title', None)
    post = Posts.query.get(id)

    if not post:
        return jsonify({'message': "post don't exist", 'data': {}}), 404

    if post.user_id != current_user.id:
        return jsonify({'message': "post don't exist", 'data': {}}), 401

    if post:
        try:
            if description:
                post.description = description
            if title:
                post.title = title
            db.session.commit()
            result = post_schema.dump(post)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except:
            return jsonify({'message': 'unable to update', 'data':{}}), 500


"""Deleta usuário com base no ID da request"""


def delete_post(current_user, id):
    post = Posts.query.get(id)
    if not post:
        return jsonify({'message': "post don't exist", 'data': {}}), 404

    if post:
        try:
            db.session.delete(post)
            db.session.commit()
            result = post_schema.dump(post)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500


def post_by_postname(current_user, postname):
    try:
        return Posts.query.filter(Posts.postname == postname).one()
    except:
        return None
