class Tiles:
    def __init__(self, num, exp):
        self.number = num
        self.exposed = exp

    #definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

my_tile = Tiles(3, True)
#your_tile = Tiles(4)

print (my_tile)
my_tile.hide_tile()
print (my_tile)
my_tile.expose_tile()
print (my_tile)

#print (my_tile.number)
#print (type(my_tile))

#print (your_tile)
#print (your_tile.number)

#print (type(your_tile))


