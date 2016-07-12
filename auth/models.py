from sqlalchemy import Column, Integer, String
from database import Base
from marshmallow import Schema

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'username')
        ordered = True


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(120), unique=True)

    # authentication method, return user instance by matching on username and validating password
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter(User.username == username).scalar()
        if user and user.validate_password(password):
            return user

    # identification method, return user instance by id
    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        return User.query.filter(User.id == user_id).scalar()

    def validate_password(self, password):

        # check first argument (hashed model password) against given password
        from service import bcrypt
        return bcrypt.check_password_hash(self.password, password)

    def __init__(self, name=None, password=None):

        self.username = name

        #hash our password
        from service import bcrypt
        self.password = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % (self.name)