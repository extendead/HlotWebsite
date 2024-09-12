# class UserLogin:
#     def fromDB(self, admin_id, database):
#         self.__user__ = database.select_id_data(admin_id)
#         return self
#
#     def create(self, user):
#         self.__user__ = user
#         return self.__user__
#
#     @property
#     def is_authenticated(self):
#         return True
#
#     @property
#     def is_active(self):
#         return True
#
#     @property
#     def is_anonymous(self):
#         return False
#
#     def get_id(self):
#         return self.__user__
#
from typing import Any

from flask_login import UserMixin


class UserLogin(UserMixin):
    def __init__(self):
        self.id = None

    def fromDB(self, user_login: Any, db: Any) -> Any:
        self.id = db.select_login_data(login=user_login)
        return self

    def create(self, user: str) -> Any:
        self.id = user
        return self

    def get_id(self) -> str:
        return str(self.id)
