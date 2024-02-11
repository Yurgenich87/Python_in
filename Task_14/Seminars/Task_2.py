import warnings

warnings.filterwarnings('ignore')

import unittest
import doctest
from Task_2 import Rectangle


class TestTask2(unittest.TestCase):
    def test_width(self):
        """Тестирование инициализации ширины"""
        r = Rectangle(5)
        self.assertEqual(r.width, 5)

    def test_height(self):
        """Тестирование инициализации ширины и высоты"""
        r = Rectangle(3, 4)
        self.assertEqual(r.height, 4)

    def test_perimeter(self):
        """Тестирование вычисления периметра"""
        r = Rectangle(5)
        self.assertEqual(r.perimeter(), 20)

    def test_area(self):
        """Тестирование вычисления площади"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_addiion(self):
        """Тестирование операции сложения прямоугольников"""
        r1 = Rectangle(5.0)
        r2 = Rectangle(3, 4)
        r3 = r1 + r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 6.0)


unittest.main()
