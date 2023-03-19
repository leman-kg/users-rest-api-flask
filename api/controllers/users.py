import os
import jwt
from dotenv import load_dotenv
from flask import request, jsonify
from datetime import datetime, timedelta

# local modules
from controllers._auth_handler import token_required
from controllers._exception_hanlder import catch_exception
import repositories.users as users_repo

load_dotenv()

@catch_exception
def login() -> str:
    """/users/login controller

    Returns:
        str: response json
    """
    response = {'success': True}

    user = users_repo.authenticate(username = request.form.get('username'), password = request.form.get('password'))

    if not user:
        return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

    token = jwt.encode({
        'sub': user.username,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        os.getenv('SECRET_KEY'),
        'HS256')
    response['token'] = token

    return jsonify(response)

@catch_exception
def create() -> str:
    """/users/create controller

    Returns:
        str: response json
    """
    response = {'success': True}
    isCreated = users_repo.create(username = request.form.get('username'),
        email = request.form.get('email'),
        password = request.form.get('password'),
        info = request.form.get('info')
    )

    if not isCreated:
        response['success'] = False

    return jsonify(response)

@token_required
@catch_exception
def list() -> str:
    """/users controller

    Returns:
        str: response json
    """
    response = {'success': True}
    response['page'] = int(request.args.get('page', 1))
    response['per_page'] = int(request.args.get('per_page', 10))

    users = users_repo.list(response['page'], response['per_page'])
    response['data'] = users

    return jsonify(response)

@token_required
@catch_exception
def get(id: int) -> str:
    """/users/<id> controller

    Returns:
        str: response json
    """
    response = {'success': True}
    user = users_repo.find_by_id(id)
    response['data'] = user

    return jsonify(response)

@token_required
@catch_exception
def update(id: int) -> str:
    """/users/update/<id> controller

    Returns:
        str: response json
    """
    response = {'success': True}
    data = request.form.to_dict()
    users_repo.update(id, data)

    return jsonify(response)

@token_required
@catch_exception
def delete(id: int) -> str:
    """/users/delete/<id> controller

    Returns:
        str: response json
    """
    response = {'success': True}
    users_repo.mark_deleted(id)

    return jsonify(response)

@token_required
@catch_exception
def purge(id: int) -> str:
    """/users/purge/<id> controller

    Returns:
        str: response json
    """
    response = {'success': True}
    users_repo.delete(id)

    return jsonify(response)
