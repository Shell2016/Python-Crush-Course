"""Класс Admin"""
from user import User


class Privileges():
    def __init__(self):
        self.privileges = ['Разрешено редактировать сообщения', 'Разрешено удалять пользователей',
                           'Разрешено удалять сообщения', 'Разрешено банить пользователей']

    def show_privileges(self):
        print('Список привилегий админа:')
        for privilege in self.privileges:
            print('  - ' + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges_list = Privileges()
