class Bike:
    # class attribute
    color = "red"

    def __init__(self, type="road", weight=45):
        self.type = type
        self.weight = weight

    def __str__(self):
        return f"the {Bike.color} {self.type} bike weighs {self.weight} grams"

    def screams(self, yell="hooray!"):
        return f"i love to ride and yell {yell} at the top of my lungs, on my big {Bike.color} {self.type} {self.weight} bike!"

    @classmethod
    def get_object(cls):
        return cls("hybrid", 22)

bike1 = Bike()
print(bike1)
Bike.color = "white"
bike2 = Bike("mountain")
print(bike2)
Bike.color = "green"
bike3 = Bike.get_object()
print(bike3)
print(bike3.screams())





