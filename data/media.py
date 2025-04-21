# ����� � ��������� ������� ����� �������

import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Media(SqlAlchemyBase):
    __tablename__ = 'media'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fname = sqlalchemy.Column(sqlalchemy.String,nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    type_of_event = sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.ForeignKey("type_of_events.id"))
    admin_id = sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.ForeignKey("admins.id"))
    admin = orm.relationship('Admin')
    event = orm.relationship('TypeOfEvents')
