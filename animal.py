class Person(object):
    MATURE_AGE = 5
    name = None
    age = 0

    def __init__(self, name, age=6, is_single=True):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def is_mature(self):

        if self.age >= self.MATURE_AGE:
            return True
        else:
            return False

    def get_sound(self):
        return None

class Dog(Animal):
    def get_sound(self):
        animal_data = super().__str__()
        return f"species: DOG, {animal_data}"

class Cat(Animal):
    def get_sound(self):
        return "Miał"

