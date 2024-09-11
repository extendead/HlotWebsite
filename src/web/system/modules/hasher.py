from werkzeug.security import generate_password_hash, check_password_hash


class Hasher:
    """ Шифратор паролей """
    @staticmethod
    def HashPassword(password: str) -> str:
        """
        :param password: Пароль
        :return: Хэш введенного пароля
        """
        __hash__ = generate_password_hash(str(password))
        return __hash__

    @staticmethod
    def UnHashPassword(password_hash: str, password: str) -> bool:
        """
        :param password_hash: Хэш пароля
        :param password: Сам пароль
        :return: True если пароль совпадает с хэшем, в противном случае False
        """
        check = check_password_hash(str(password_hash), str(password))
        return check
