from flask import jsonify
from functools import wraps

def catch_exception(f):
    @wraps(f)
    def _try(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            code = 500
            response = {'success': False}
            response['message'] = "\n".join(e.args)

            if isinstance(e, ValueError):
                code = 400

            return jsonify(response), code

    return _try
