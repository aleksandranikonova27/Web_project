# Класс с описанием таблицы пользователей

import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Admin(SqlAlchemyBase, UserMixin):
    __tablename__ = 'admins'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    stutus = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    posts = orm.relationship("Media", back_populates='admin')

    def __repr__(self):
        return f'{self.name} - {self.email} - {self.created_date}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
