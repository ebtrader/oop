# https://realpython.com/python3-object-oriented-programming/

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)

print(miles.description())

print(miles.speak('Woof Woof'))

print(miles.speak('Bow Wow'))







