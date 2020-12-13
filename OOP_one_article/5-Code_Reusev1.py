# OOP tutorial
# 5 Code Reuse
# https://towardsdatascience.com/understand-o-o-p-in-python-with-one-article-bfa76f3ba48c

class Bikes():
    def __init__(self, terrain, size):
        self.terrain = terrain
        self.size = size

class Road(Bikes):
    pass

class Mountain(Bikes):
    pass

love_road = Road('highway', 'large')

print(love_road.terrain)
print(love_road.size)

