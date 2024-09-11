from mysql.connector.errors import Error
from src.database import Database
from src.web.system.modules.hasher import Hasher

from colorama import Back


class Check:
    @staticmethod
    def CheckPhone(phone_num: str) -> bool:
        """
        :param phone_num: Номер телефона для проверки
        :return: True если длина номера телефона состоит из цифр и соответствует, в противном случае False
        """
        phone_num = phone_num.split('+')[1] if phone_num.startswith('+') else phone_num
        result = True if len(phone_num) == 11 and phone_num.isdigit() else False
        return result

    @staticmethod
    def CheckAdminLoginData(login: str, password: str) -> bool:
        """
        :param login: Логин админа
        :param password: Пароль админа
        :return: True если пароль соответствует паролю в базе, в противном случае False
        """
        try:
            db = Database()
            result = db.select_login_data(login=login)
            data = {
                'login': result[1],
                'password': result[2]
            }
            check_res = Hasher.UnHashPassword(data['password'], password)
            return check_res
        except TypeError as e:
            print(Back.RED + f"Ошибка логина! {e}")
            return False
