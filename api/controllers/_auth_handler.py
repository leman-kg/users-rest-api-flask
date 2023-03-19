import os
import jwt
from flask import jsonify, request
from dotenv import load_dotenv
from functools import wraps

# local modules
import repositories.users as users_repo

load_dotenv()

def token_required(f):
    """Decorator for controllers that checks if the user is authenticated
    """
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'success': False,
            'message': 'Invalid token. Registeration and / or authentication required'
        }
        expired_msg = {
            'success': False,
            'message': 'Expired token. Reauthentication required.'
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, os.getenv('SECRET_KEY'), ['HS256'])
            user = users_repo.find_by_username(data['sub'], False)
            if not user:
                raise RuntimeError('User not found')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            invalid_msg['error'] = e.args[0]
            return jsonify(invalid_msg), 401

    return _verify
