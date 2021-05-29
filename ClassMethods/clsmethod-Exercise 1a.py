class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)

std = Student.getobject()
print(std.name)
print(std.age)
