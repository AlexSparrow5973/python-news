from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    mail = db.Column(db.String(50), unique=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)  # хешируем пароль

    def check_password(self, password):
        # хешируем пароль и сравниваем его с хранимым в базе данных
        return check_password_hash(self.password, password)

    @property  # позволяет использовать метод как атрибут класса
    def is_admin(self):
        return self.role == "admin"  # возвращает True если role == "admin"

    def __repr__(self):
        return 'User {}'.format(self.username)
