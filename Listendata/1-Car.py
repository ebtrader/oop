class Car:
    def __init__(self, year=2016, mpg=20, speed=100):
        self.year = year
        self.mpg = mpg
        self.speed = speed

    def accelerate(self):
        accel = self.speed + 10
        return f"The car accelerated to {accel} mph"

    def brake(self):
        brk = self.speed - 10
        return f"The car slowed to {brk} mph"
        # return f"The car accelerated to {self.accelerate()} mph"

car1 = Car()

print(car1.accelerate())
print(car1.brake())
print(car1.year)
print(car1.mpg)
print(car1.speed)