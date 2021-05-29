# https://www.w3schools.com/python/python_inheritance.asp

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):

pers1 = Person("John", "Smith")
pers1.printname()
pers2 = Student("jane", "doe")
pers2.printname()




