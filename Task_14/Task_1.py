import warnings

warnings.filterwarnings('ignore')

import doctest

class NegativeValueError(Exception):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        """

        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r4 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        >>> r3 = Rectangle(-3, -4)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -3
        >>> r4 = Rectangle(3, -4)
        Traceback (most recent call last):
        ...
        NegativeValueError: Высота должна быть положительной, а не -4


        """
        if width < 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        if height is not None and height < 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        self.width = width
        self.height = height if height is not None else width

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        return self.width * self.height

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 =Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        return Rectangle(new_width, new_height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


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
    #first_line = file.readline()
    #first_five_lines = lines[:1]

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
