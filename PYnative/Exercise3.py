# https://pynative.com/python-object-oriented-programming-oop-exercise/

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return "Vehicle Name: " + self.name + " Speed: " + str(self.max_speed) + " Mileage: " + str(self.mileage)

# child and parent inheritance
class Bus(Vehicle):
    pass

# modelX = Vehicle(80, 23)

# print(modelX.max_speed, modelX.mileage)

sample_bus = Bus("School Volvo", 180, 12)
print(sample_bus)



