#class Cat:
#    pass

class Cat:
    def __init__(self, number, color, size="really big"):
        self.number = number
        self.color = color
        self.size = size

    def __str__(self):
        return "the " + str(self.number) + " " + self.color + " cats are of " + self.size + " size."

    def cat_noise(self, sound):
        return f"the {self.color} cat makes a {sound}-ing sound."

# created a child class of parent "Cat"
class Tiger(Cat):
    pass

cat1 = Cat(15, "black")

print(cat1)

print(cat1.cat_noise("purrrrrr"))

Joey = Tiger(13, "white")

print(Joey)
#print(Joey.cat_noise("roar"))

tiger_roar = Joey.cat_noise("roar")

#print(tiger_roar)
print("I heard " + tiger_roar)
