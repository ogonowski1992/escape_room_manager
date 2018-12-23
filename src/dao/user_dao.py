import hashlib
import uuid

from src.database import db_session
from src.entities.user import User


def login(username, password):
    hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
    user = User.query.filter(User.username == username, User.password == hashed_password).first()
    return user


def check_if_username_exist(username):
    user = User.query.filter(User.username == username).first()
    return user is not None


def registration(username, password, name, surname):
    hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

    u = User(username, hashed_password, name, surname)
    db_session.add(u)
    db_session.commit()
    return u
