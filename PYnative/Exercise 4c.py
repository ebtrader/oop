# class Language:
#     pass
#
# lang1 = Language()
# print(lang1)
#
# lang1.name = "python"
# print(lang1.name)

class Language:
    character = "zen"

    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return f"This language has {self.number} styles and has the color {self.color} with character {Language.character}"

    def multiplier(self):
        prod = self.number*4
        return f"the product is {prod}"

lang1 = Language(5, "red")
print(lang1)
print(lang1.multiplier())


