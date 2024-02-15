import argparse
import json
import os
import logging

# Получаем абсолютный путь к текущему каталогу
import pytest

log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
log_file = os.path.join(log_directory, 'log.log')

# Проверяем наличие каталога для логов, и создаем его, если он не существует
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
'в строке {lineno:03d} функция "{funcName}()" ' \
'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, filename='log.log', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Task_15')


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
        if not os.path.exists(file_name):
            logger.error(f'Файл {file_name} не найден.')
            return set()
        self.users = set()
        try:
            with open(file_name, encoding='utf-8') as f:
                file_dict = json.load(f)
                for lvl, dict_ in file_dict.items():
                    for id_, name in dict_.items():
                        self.users.add(User(name, id_, lvl))
        except FileNotFoundError:
            logger.error(f'Файл {file_name} не найден.')
        except json.decoder.JSONDecodeError:
            logger.error(f'Ошибка декодирования JSON файла: {file_name}. Файл имеет неправильный формат.')
        return self.users

    def login(self, name: str, id_: str) -> bool:
        temp_user = User(name, id_, 0)
        for user in self.users:
            if user == temp_user:
                self.active_user = user
                logger.info(f'Пользователь {name} c id: {id_} успешно зарегистрирован!')
                break
        else:
            error_msg = f'Пользователь {name} c id: {id_} не найден при попытке входа.'
            logger.exception(error_msg)
            raise AccessError(name, id_)

    def add_user(self, name, id_, level):
        if not self.active_user:
            logger.error("Необходимо войти в систему для добавления нового пользователя.")
            raise AccessError("Необходимо войти в систему для добавления нового пользователя.")
        try:
            level = int(level)
            if not 1 <= level <= 7:
                raise ValueError("Уровень доступа должен быть от 1 до 7.")
        except ValueError as e:
            logger.error(f"Ошибка при добавлении пользователя: {name}")
            raise
        if self.active_user and level >= self.active_user.level:
            new_user = User(name, id_, level)
            self.users.add(new_user)
            logger.info(f'Добавлен новый пользователь {name} c id: {id_}.')
            return new_user
        else:
            error_msg = 'Невозможно добавить пользователя. Уровень доступа слишком низкий.'
            logger.exception(error_msg)
            raise LevelException()


def __create_json(file_name: str, dict_: dict):
    """Create json files"""
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dict_, f, indent=2, ensure_ascii=False)
        logger.info("Файл json открыт успешно!")


def __update_json(file_name: str, name: str, id_: str, level: str):
    """Adding data to json files"""
    try:
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
            logger.debug(f'Такой id {id_} уже существуют')
            raise ValueError(f'Такой id {id_} уже существуют')
        file_dict[level] = file_dict.get(level, {}) | {id_: name}
        __create_json(file_name, file_dict)
    except Exception as e:
        logger.error(f'Ошибка при записи данных в файл JSON: {e}')
        raise


def task2(file_name):
    while True:
        name = input('Введите имя: ') or 'Юрий'
        id_ = input('Введите личный идентификатор: ') or '10'
        level = input('Введите уровень доступа (от 1 до 7): ') or '5'
        if not os.path.exists(file_name):
            __create_json(file_name, {level: {id_: name}})
        else:
            try:
                __update_json(file_name, name, id_, level)
            except ValueError as e:
                print(e)
        exit_choice = input('Для завершения введите Exit, для продолжения нажмите Enter: ')
        if exit_choice.lower() == 'exit':
            logger.info('Завершили программу вводом: exit')
            logger.info("Программа успешно завершила свою работу.")
            break


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', type=str, help='Name of the JSON file')
    args = parser.parse_args()

    if args.filename:
        task2(args.filename)
    else:
        print(" Введите: python имя_файла.py --filename имя_файла.json в терминале")



@pytest.fixture
def project():
    return Project()


# Функция для считывания логов и проверки сообщений
def check_logs(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        logs = f.readlines()
        for log in logs:
            print(log.strip())


# Проверка логирования при успешном входе пользователя
def test_successful_login(project):
    project.get_users(FILE_NAME)
    project.login('Yuriy', '1')
    check_logs('log.log')


# Проверка логирования при неудачном входе пользователя
def test_failed_login(project):
    project.get_users(FILE_NAME)
    try:
        project.login('NonExistingUser', '123')
    except AccessError as e:
        pass
    check_logs('log.log')


# Проверка логирования при успешном добавлении нового пользователя
def test_successful_add_user(project):
    project.get_users(FILE_NAME)
    project.login('Yuriy', '1')
    try:
        project.add_user('NewUser', '456', 5)
    except LevelException as e:
        pass
    check_logs('log.log')


# Проверка логирования при неудачной попытке добавления нового пользователя
def test_failed_add_user(project):
    project.get_users(FILE_NAME)
    project.login('Yuriy', '1')
    try:
        project.add_user('NewUser', '789', 1)
    except AccessError as e:
        pass
    check_logs('log.log')


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', type=str, help='Name of the JSON file')
    parser.add_argument('--name', type=str, help='Name of the user for login or adding')
    parser.add_argument('--id', type=str, help='ID of the user for login or adding')
    parser.add_argument('--level', type=str, help='Access level of the user for adding')
    args = parser.parse_args()

    if args.filename:
        # Вызовите нужные функции, передав значения аргументов из командной строки
        project = Project()
        project.get_users(args.filename)
        if args.name and args.id:
            project.login(args.name, args.id)
        elif args.name and args.id and args.level:
            project.add_user(args.name, args.id, args.level)
        else:
            task2(args.filename)
    else:
        print("""имя_файла.py - это имя сценария Python.
--filename имя_файла.json - указывает путь к JSON-файлу, с которым вы хотите работать.
--name имя - указывает имя пользователя для входа или добавления.
--id идентификатор - указывает идентификатор пользователя для входа или добавления.
--level уровень_доступа - указывает уровень доступа пользователя для добавления.
Пример: python Task_1.py --filename name.json --name 'Валя' --id 123 --level 3""")


if __name__ == "__main__":
    main()


