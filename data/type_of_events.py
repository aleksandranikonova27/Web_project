import sqlalchemy
from .db_session import SqlAlchemyBase


class TypeOfEvents(SqlAlchemyBase):
    __tablename__ = 'type_of_events'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    events = sqlalchemy.Column(sqlalchemy.String, nullable=True)
