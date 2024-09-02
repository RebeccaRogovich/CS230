import unittest
from classprogram import Dog  

class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog(name="Buddy", breed="Golden Retriever")

    def test_make_sound(self):
        self.assertEqual(self.dog.make_sound(), "Woof!")

    def test_fetch(self):
        item = "ball"
        self.assertEqual(self.dog.fetch(item), "Buddy is fetching the ball!")

    def test_sit(self):
        self.assertEqual(self.dog.sit(), "Buddy sits obediently.")

    def test_attributes(self):
        self.assertEqual(self.dog.name, "Buddy")
        self.assertEqual(self.dog.species, "Dog")
        self.assertEqual(self.dog.breed, "Golden Retriever")

if __name__ == "__main__":
    unittest.main()
