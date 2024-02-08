class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name or not isinstance(last_name, str):
            raise InvalidNameError("Invalid name: {}. Name should be a non-empty string.".format(last_name))
        if not first_name or not isinstance(first_name, str):
            raise InvalidNameError("Invalid name: {}. First name should be a non-empty string.".format(first_name))
        if not middle_name or not isinstance(middle_name, str):
            raise InvalidNameError("Invalid name: {}. Middle name should be a non-empty string.".format(middle_name))
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError("Invalid age: {}. Age should be a positive integer.".format(age))
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, employee_id):
        super().__init__(last_name, first_name, middle_name, age)
        if not isinstance(employee_id, int) or not (100000 <= employee_id <= 999999):
            raise InvalidIdError("Invalid id: {}. Id should be a 6-digit positive integer between 100000 and 999999.".format(employee_id))
        self.employee_id = employee_id

    def get_level(self):
        return sum(int(digit) for digit in str(self.employee_id)) % 7


person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
