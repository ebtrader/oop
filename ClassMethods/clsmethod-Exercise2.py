class Pizza:
    radius = 42

    @classmethod
    def get_radius(cls):
        return cls.radius

pizza1 = Pizza.get_radius()
print(pizza1)
