class Tiles:
    def __init__(self, num):
        self.number = num

    #definition of getter for number
    def get_number(self):
        return self.number

my_tile = Tiles(3)
your_tile = Tiles(4)

print (my_tile)
print (my_tile.number)
#print (type(my_tile))

print (your_tile)
print (your_tile.number)

#print (type(your_tile))


