# Класс с описанием таблицы заказов

import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from flask_login import UserMixin


class Order(SqlAlchemyBase, UserMixin):
    __tablename__ = 'orders'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    wishes = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    need_date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    count_of_people = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    type_of_events = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("event.id"))
    event = orm.relationship('TypeOfEvents')
    def __repr__(self):
        return f'{self.name} - {self.phone_number} - {self.created_date}'