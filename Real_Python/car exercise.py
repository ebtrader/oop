class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles."

blue_car = Car('blue', 20_000)
print(blue_car)

red_car = Car('red', 23_000)
print(red_car)

#or another way is

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")

# the :, is a format specifier