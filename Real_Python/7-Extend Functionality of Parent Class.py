# https://realpython.com/python3-object-oriented-programming/

class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

     # def speak(self, sound):
    #     return f"{self.name} says {sound}"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"

# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
# print(miles.speak("Grrr"))

jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))
