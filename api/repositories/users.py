from werkzeug.security import check_password_hash

# local modules
from services.database import db
from models.user import User

def authenticate(username: str, password: str) -> User:
    """Authentication using username and password

    Args:
        username (str)
        password (str)

    Returns:
        User: user model
    """
    user = User.query.filter_by(username = username).first()
    if not user or not check_password_hash(user.password, password):
        return None

    return user

def create(username: str, email: str, password: str, info: str|None) -> bool:
    """create new user in the DB

    Args:
        username (str)
        email (str)
        password (str)
        info (str | None)

    Raises:
        RuntimeError: if user doesn't exist

    Returns:
        bool: True - if created, False - if not
    """
    user = User.query.filter((User.email == email) | (User.username == username)).first()

    if user:
        raise RuntimeError('User with such username or email already exists')

    newUser = User(
        id = None,
        username = username,
        email = email,
        password = password,
        info = info
    )
    db.session.add(newUser)
    db.session.commit()

    return True

def list(page:int = 1, per_page:int = 20, hide_password: bool = True) -> list:
    """Get a list of dicts with user info; with pagination

    Args:
        page (int, optional): the page number. Defaults to 1.
        per_page (int, optional): Amount of users per page. Defaults to 20.
        hide_password (bool, optional): if True, excludes the password hash from the dicts. Defaults to True.

    Raises:
        RuntimeError: if list is empty

    Returns:
        list: list of dicts with user info
    """
    users = db.paginate(db.select(User), page = page, per_page = per_page)

    if not users:
        raise RuntimeError('No users in the system')

    users = [user.to_dict(hide_password) for user in users]

    return users

def find_by_id(id: int, hide_password: bool = bool) -> dict:
    """Get a dict with user's info by its id

    Args:
        id (int): id of the user you are looking for
        hide_password (bool, optional): if True, excludes the password hash from the dict. Defaults to bool.

    Raises:
        RuntimeError: if no user with provided id found

    Returns:
        dict: user info
    """
    user = User.query.filter_by(id = id).first()

    if not user:
        raise RuntimeError('User not found')

    return user.to_dict(hide_password)

def find_by_username(username: str, hide_password: bool = bool) -> dict:
    """Get a dict with user's info by its username

    Args:
        username (str): username of the user you are looking for
        hide_password (bool, optional): if True, excludes the password hash from the dict. Defaults to bool.

    Raises:
        RuntimeError: if no user with provided username found

    Returns:
        dict: user info
    """
    user = User.query.filter_by(username = username).first()

    if not user:
        raise RuntimeError('User not found')

    return user.to_dict(hide_password)

def update(id: int, data) -> bool:
    """Change user's data

    Args:
        id (int)

    Raises:
        RuntimeError: if user is not found

    Returns:
        bool: True - if updated succesfully
    """
    user = User.query.filter_by(id = id).first()

    if not user:
        raise RuntimeError('User not found')

    for field in data:
        setattr(user, field, data[field])

    db.session.commit()

    return True

def mark_deleted(id: int) -> bool:
    """Soft delete by updating deleted_at column

    Args:
        id (int): user id

    Raises:
        RuntimeError: if user is not found

    Returns:
        bool: True - if updated succesfully
    """
    user = User.query.filter_by(id = id).first()

    if not user:
        raise RuntimeError('User not found')

    user.deleted_at = db.func.now()
    db.session.commit()

    return True

def delete(id: int) -> bool:
    """Remove the record from the table

    Args:
        id (int): user's id

    Raises:
        RuntimeError: if user is not found

    Returns:
        bool: True - if removed succesfully
    """
    user = User.query.filter_by(id = id).first()

    if not user:
        raise RuntimeError('User not found')

    db.session.delete(user)
    db.session.commit()

    return True
