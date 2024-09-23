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
