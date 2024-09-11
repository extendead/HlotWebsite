from mysql.connector import Connect
from mysql.connector.errors import Error

from colorama import init, Fore, Back
from typing import Any


class Database:
    def __init__(self):
        """ Инициализация """
        init(autoreset=True)
        self.con = Connect(
            host='localhost',
            user="root",
            password="UM8$7I9o",
            database="script_data"
        )
        self.cur = self.con.cursor()

#   #~#~#~# [ users ] #~#~#~#
    def add_user(self, user_name: str, phone: str,
                 email: str, fb_text: str,
                 social_media: str) -> None:
        """
        :param user_name: Имя пользователя
        :param phone: Номер телефона
        :param email: Почта
        :param fb_text: Текст обращения
        :param social_media: Соцсеть для связи, по умолчанию идет WhatsApp
        """
        try:
            self.cur.execute(""" INSERT INTO users (user_name, phone, email, fb_text, social_media)
                                          VALUES (%s, %s, %s, %s, %s) """,
                             (user_name, phone, email, fb_text, social_media))
            self.con.commit()
            print(Back.GREEN + "Пользователь успешно добавлен!")
        except Error as e:
            print(Back.RED + f"Ошибка добавления пользователя в базу! {e}")

#   #~#~#~# [ admin ] #~#~#~#
    def select_login_data(self, login: str) -> Any:
        """
        :param login: Логин админа
        :return: Логин и пароль для входа в админ-панель по логину
        """
        try:
            self.cur.execute(""" SELECT * FROM admin_data WHERE login = %s """, (login,))
            return self.cur.fetchone()
        except Error as e:
            print(Back.RED + f"Ошибка вывода логина и пароля! {e}")
