class NegativeValueError(ValueError):
    pass

class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self._height = height if height is not None else width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._validate_positive(value, "высота")
        self._height = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._validate_positive(value, "ширина")
        self._width = value

    def _validate_positive(self, value, dimension_name):
        if value < 0:
            raise NegativeValueError(f"{dimension_name.capitalize()} должна быть положительной, а не {value}")

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other):
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


r = Rectangle(4, 4)
r.width = -3
