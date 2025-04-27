import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm

class TypeOfEvents(SqlAlchemyBase):
    __tablename__ = 'type_of_events'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    events = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    event1 = orm.relationship("Media", back_populates='id')
    event2 = orm.relationship("Order", back_populates='id')
