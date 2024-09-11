from src.database import Database as db


class UserLogin:
    def fromDB(self, login: str):
        self.__user = db.select_login_data(login=login)
        return self

    def create(self, user):
        self.__user == user
        return self

    def is_authentication(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['login'])
