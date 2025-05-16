from flask_jwt_extended import create_access_token

from Models.userModel import UserModel
from database import db

def authenticate_user(username, password):
    user = UserModel.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return create_access_token(identity=username)
    return None


def register_user(username, password):
    if UserModel.query.filter_by(username=username).first():
        return None  # Usuario ya existe
    new_user = UserModel(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user