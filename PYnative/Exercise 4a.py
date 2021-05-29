# class Geek:
#     pass

class Geek:
    def __init__(self, language, years):
        self.language = language
        self.years = years

    def __str__(self):
        return "The language is " + self.language + " and the number of years experience is " + str(self.years) + "."

    def what_he_says(self, sound):
        return f"This is {sound} hard!"

# class Expert(Geek):
#     pass

# class Expert(Geek):
#     def what_he_says(self, sound="damn"):
#         return f"I can't do this {sound} thing!"

class Expert(Geek):
    def what_he_says(self, sound="damn"):
        return super().what_he_says(sound)

programmer1 = Geek("python", 5)
programmer2 = Geek("java", 4)
print(programmer1, programmer2)

programmer3 = Expert("C++", 4)
print(programmer3)

print(programmer1.what_he_says("freaking"))
print(programmer3.what_he_says())


