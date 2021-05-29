# class Exercise:
#     pass

class Exercise:
    # class attribute
    color = "white"

    def __init__(self, type, days):
        self.type = type
        self.days = days

    def __str__(self):
        return f"I do {self.type} {self.days} days a week"

    def screams(self, sound="got it!"):
        return f"I yell {sound} when I work out playing {self.type} {self.days} days a week"

    @classmethod
    def get_object(cls):
        return cls("football", 43)

# class Expert(Exercise):
#     pass

# class Expert(Exercise):
#     def screams(self, sound="yes"):
#         return f"We don't yell, we say {sound}"

class Expert(Exercise):
    def screams(self, sound="yes"):
        return super().screams(sound)

    def location(self, place):
        return f"I usually play {self.type} at the {place} {self.days} days a week wearing a {Exercise.color} shirt"

guy1 = Exercise("yoga", 3)

print("Guy1: ", guy1)
print("Guy1: ", guy1.screams("ouch"))
print("Guy1: ", guy1.screams())

guy2 = Expert("tennis", 4)
print("Guy2: ", guy2.screams())

guy3 = Expert("soccer", 2)
print("Guy3: ", guy3.location("soccer field"))
print("Guy3: ", guy3)

guy4 = Exercise("baseball", 3)
print("Guy4: ", guy4.screams())
print("Guy4: ", guy4.screams("homerun!"))

guy5 = Exercise.get_object()
print("Guy5: ", guy5)

