from os import path

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, create_engine
from sqlalchemy.orm import relationship, Session, sessionmaker

DB_NAME = 'database.db'
engine = create_engine(f'sqlite:///{DB_NAME}', echo=True, future=True)
session = Session(engine)
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    role = Column(String(150))
    date = Column(DateTime(timezone=True), server_default=func.now())
    activity = relationship('Activity')


class Activity(db.Model):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), ForeignKey('user.id'))
    distance = Column(Integer())
    time_create = Column(DateTime(timezone=True), server_default=func.now())
    time_update = Column(DateTime(timezone=True), onupdate=func.now())


def create_db_app():
    if not path.exists(f'/{DB_NAME}'):
        db.metadata.create_all(engine)
