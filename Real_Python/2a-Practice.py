#class Dog:
#    pass

#dog_name = input("Give me a dog's name: ")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return"The dog's name is " + self.name + " and its age is " + str(self.age) + "."

    #instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks {sound}"

#buddy = Dog(dog_name, 10)
rufus = Dog("Rufus", 7)

#print(buddy, rufus)
#print(rufus.description())

print(rufus.speak("Bow wow"))





