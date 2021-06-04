class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)

class Bus(Vehicle):
    def seating_capacity(self, capacity=20):
        return super().seating_capacity(capacity)

# class Bus(Vehicle):
#     def seating_capacity(self, capacity=20):
#         return "No seating capacity"

School_bus = Bus("bus", 180, 12)
print(School_bus.seating_capacity())

