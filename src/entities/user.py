from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from src.database import Base


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(512))
    name = Column(String(120))
    surname = Column(String(120))

    def __init__(self, username=None, password=None, name=None, surname=None):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
