from sqlalchemy import Column, Integer, String

from src.database import Base


class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    street = Column(String(120))
    city = Column(String(120))
    number = Column(String(20))

    def __init__(self, name=None, email=None, street=None, city=None, number=None):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.number = number
