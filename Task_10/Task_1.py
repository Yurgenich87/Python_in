



class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return f"{self.wingspan / 2}"


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        minimum = 1
        maximum = 100
        delta = 0
        delta = min(100, max(10, delta))
        if self.max_depth < 10:
            return minimum
        elif self.max_depth > 100:
            return maximum
        else:
            return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return f"Малявка"
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            raise ValueError("Недопустимый тип животного")


animal4 = AnimalFactory.create_animal('Spider', 'Elephant', 5000)
print(animal4.category())
