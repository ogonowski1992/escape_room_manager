import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime

from src.database import Base


class VisitedRooms(Base):
    __tablename__ = 'visited_rooms'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime, default=datetime.datetime.utcnow)
    escape_time = Column(Integer)

    def __init__(self, room_id=None, user_id=None, date=None, escape_time=0):
        self.room_id = room_id
        self.user_id = user_id
        self.date = date
        self.escape_time = escape_time
