class Car:
    def __init__(self, color, model, shape):
        self.color = color
        self.model = model
        self.shape = shape

    def __str__(self):
        return "The car is " + self.color + " and model is " + self.model + " and series is " + self.shape + "."

    def draw(self):
        pass

    def drag(self):
        pass

    def change_color(self):
        pass

car1 = Car("blue", "Ford", "coupe")
car2 = Car("red", "Nissan", "SUV")

print(car1)
print(car2)

