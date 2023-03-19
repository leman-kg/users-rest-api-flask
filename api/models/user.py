import re
from werkzeug.security import generate_password_hash

# local modules
from services.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    deleted_at = db.Column(db.DateTime)
    password = db.Column(db.String(255), nullable=False)
    info = db.Column(db.String)

    def __init__(
        self,
        id: int|None,
        username: str,
        email: str,
        password: str,
        info: str|None,
    ) -> dict|None:
        self.id = id
        self.username = username
        self.email = email
        self.password = generate_password_hash(password, method='sha256')
        self.info = info

        isValid, message = self.validate()
        if not isValid:
            raise ValueError(message)

    def to_dict(self, hide_password: bool = True) -> dict:
        """Convert the model into a dict

        Args:
            hide_password (bool, optional): True - excludes the password field from the dict. Defaults to True.

        Returns:
            dict: dict with user info
        """
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}

        if hide_password:
            result.pop('password')

        return result

    def validate(self) -> tuple [bool, str]:
        """Validate model fields

        Returns:
            tuple [bool, str]: value #1: True - if the fields are valid returns; value #2: additional info if any field is invalid
        """
        if not re.search(r"^[\w\d\.\_\-]+$", self.username):
            return False, 'Username can contain only letters, digits, dots (.), dashes (-), and unserscores (_)'

        if not re.search(r"^[\w\d\.\_\-\%\+]+@[\w\d\.\_\-\%\+]+\.[A-Z|a-z]{2,7}$", self.email):
            return False, 'Email address format is incorrect'

        return True, ''
