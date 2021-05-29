# https://pynative.com/python-object-oriented-programming-oop-exercise/

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(80, 23)

print(modelX.max_speed, modelX.mileage)





