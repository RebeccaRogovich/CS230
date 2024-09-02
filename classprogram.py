class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self, item):
        return f"{self.name} is fetching the {item}!"

    def sit(self):
        return f"{self.name} sits obediently."
