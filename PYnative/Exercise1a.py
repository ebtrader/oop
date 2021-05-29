class Sushi:
    def __init__(self, roll_type, roll_number):
        self.roll_type = roll_type
        self.roll_number = roll_number

    def __str__(self):
        return "You ordered a " + self.roll_type + " roll and the quantity is " + str(self.roll_number) + "."

order1 = Sushi("spider", 3)
order2 = Sushi("dragon", 2)
print (order1, order2)




