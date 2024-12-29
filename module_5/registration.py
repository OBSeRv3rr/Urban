class DataBase:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        if user.is_valid_password():
            self.data[user.username] = user.password
            print(f"Пользователь {user.username} успешно добавлен.")
        else:
            print(f"Пароль пользователя {user.username} не соответствует требованиям.")


class User:
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    def is_valid_password(self):
        if len(self.password) < 8:
            return False
        if not any(char.isdigit() for char in self.password):
            return False
        if not any(char.isupper() for char in self.password):
            return False
        return True


if __name__ == '__main__':
    db = DataBase()
    while True:
        choice = input('Выбирите действие: \n1 - Вход \n2 - Регистрация\n')
        if choice == '1':
            login = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            if login in db.data:
                if password == db.data[login]:
                    print('Приветствую, ', login)
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == '2':
            user = User(input('Введите имя пользователя: '),
                        password := input('Введите пароль: '),
                        password2 := input('Подтвердите пароль: '))
            if password != password2:
                print('Пароли не совпадают')
                continue
            db.add_user(user.username, user.password)

        print(db.data)
