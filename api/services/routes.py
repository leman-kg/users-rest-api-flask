from flask import Blueprint

# local modules
from controllers.users import login, list, create, get, update, delete, purge

# default routes
default = Blueprint('default', __name__)
default.route('/login', methods=['POST'])(login)

# users routes
users = Blueprint('users', __name__, url_prefix = '/users')
users.route('/', methods=['GET'])(list)
users.route('/create', methods=['POST'])(create)
users.route('/<int:id>', methods=['GET'])(get)
users.route('/update/<int:id>', methods=['POST'])(update)
users.route('/delete/<int:id>', methods=['DELETE'])(delete)
users.route('/purge/<int:id>', methods=['DELETE'])(purge)
