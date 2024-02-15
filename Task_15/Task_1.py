import json
import os

FILE_NAME = 'name.json'


class MyException(Exception):
    pass


class LevelException(MyException):
    def __init__(self):
        pass

    def __str__(self):
        return f'Нельзя создать пользователя без входа и когда Ваш уровень ниже меньше допустимого'


class AccessError(MyException):
    def __init__(self, name, id_):
        self.name, self.id = name, id_

    def __str__(self):
        return f'Пользователь {self.name} c id: {self.id}  не найден.'


class User:

    def __init__(self, name: str, id_: str, level: str):
        self.name = name
        self.id = int(id_)
        self.level = int(level)

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id and self.name == other.name

    def __str__(self):
        return f'Имя: {self.name}, id: {self.id}, level: {self.level}'

    def __hash__(self):
        return hash((self.name, self.id))


class Project:
    def __init__(self):
        self.active_user = None
        self.users = set()

    def get_users(self, file_name: str) -> set:
        with open(file_name, encoding='utf-8') as file:
            try:
                file_dict = json.load(file)
            except json.decoder.JSONDecodeError:
                file_dict = {}
            for lvl, dict_ in file_dict.items():
                for id_, name in dict_.items():
                    self.users.add(User(name, id_, lvl))
        return self.users

    def login(self, name: str, id_: str) -> bool:
        temp_user = User(name, id_, 0)
        for user in self.users:
            if user == temp_user:
                self.active_user = user
                break
        else:
            raise AccessError(name, id_)

    def add_user(self, name, id_, level):
        if self.active_user and level >= self.active_user.level:
            new_user = User(name, id_, level)
            self.users.add(User(name, id_, level))
            return new_user
        else:
            raise LevelException()


def __create_json(file_name: str, dict_: dict):
    """Create json files"""
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dict_, f, indent=2, ensure_ascii=False)


def __update_json(file_name: str, name: str, id_: str, level: str):
    """Adding data to json files"""
    with open(file_name, encoding='utf-8') as f:
        try:
            file_dict = json.load(f)
        except json.decoder.JSONDecodeError:
            file_dict = {}
    id_list = []
    for level in file_dict:
        for id_dict in file_dict[level]:
            id_list.append(id_dict)
    if id_ in id_list:
        raise ValueError(f'Такой id {id_} уже существуют')
    file_dict[level] = file_dict.get(level, {}) | {id_: name}
    __create_json(file_name, file_dict)


def task2(file_name):
    while True:
        name = input('Введите имя') or 'Юрий'
        id_ = input('Введите личный идентификатор: ') or '10'
        level = input('Введите уровень доступа (от 1 до 7):') or '5'
        if not os.path.exists(file_name):
            __create_json(file_name, {level: {id_: name}})
        else:
            try:
                __update_json(file_name, name, id_, level)
            except ValueError as e:
                print(e)
        exit_choice = input('Для завершения введите Exit, для продолжения нажмите Enter: ')
        if exit_choice.lower() == 'exit':
            break


def save_files_csv():
    pass


if __name__ == '__main__':
    project = Project()
    print(*project.get_users(FILE_NAME), sep='\n')
    print('-' * 20)
    project.login('Yuriy', '6')
    print(f'Нашел пользователя: {project.active_user}')
    print('-' * 20)
    print(project.add_user('Vladimir', 4, 5))
