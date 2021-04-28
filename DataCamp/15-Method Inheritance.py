class Player:
    MAX_POSITION = 10
    MAX_SPEED = 3

    def __init__(self):
        self.position = 0


# Create a Racer class and set MAX_SPEED to 5
class Racer(Player):
    MAX_SPEED = 5


# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)