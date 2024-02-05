class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100
        print(f'{id(self) = }')

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

p1 = Person()


print(f"{p1.health = }")
