import warnings

warnings.filterwarnings('ignore')

import doctest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def test_employee_full_name():
    """
    >>> emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, '1', 20000)
    >>> emp.full_name()
    'Ivanov Ivan Ivanovich'
    """


def test_employee_birthday():
    """
    >>> emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, '1', 20000)
    >>> emp.birthday()
    >>> emp.get_age()
    31
    """


def test_employee_raise_salary():
    """
    >>> emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
    >>> emp.raise_salary(10)
    >>> emp.salary
    55000.0
    """


def test_employee_str():
    """
    >>> emp = Employee('Ivanov', 'Ivan', 'Ivanovich', 30, 'manager', 50000)
    >>> emp.__str__()
    'Ivanov Ivan Ivanovich (Manager)'
    """


def test_employee_last_name_title():
    """
    >>> emp = Employee('ivanov', 'ivan', 'ivanovich', 30, 'manager', 50000)
    >>> emp.last_name
    'Ivanov'
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


import sys

# Открываем файл для записи
with open('pytest_output.txt', 'w') as file:
    # Перенаправляем stdout в файл
    sys.stdout = file

    # Запускаем pytest.main() с нужными параметрами
    __file__ = None

    doctest.testmod(extraglobs={'__file__': __file__})

# Возвращаем stdout в исходное состояние
sys.stdout = sys.__stdout__
# Считываем содержимое файла
with open('pytest_output.txt', 'r') as file:
    lines = file.readlines()
    # first_line = file.readline()
    # first_five_lines = lines[:1]

import re

file_name = "pytest_output.txt.txt"

# Открываем файл на чтение
with open('pytest_output.txt', "r") as file:
    # Считываем содержимое файла
    file_content = file.read()

# Используем регулярное выражение для удаления "line" и чисел после него
cleaned_content = re.sub(r'File "__main__", line \d+', '', file_content)

# Записываем обновленное содержимое обратно в файл
with open(file_name, "w") as file:
    file.write(cleaned_content)

with open(file_name, 'r') as new_file:
    file_contents = new_file.read()
    # Выводим содержимое файла на экран
    print(file_contents)
