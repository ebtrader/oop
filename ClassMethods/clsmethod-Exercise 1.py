class Student:
    name = "barbara"
    subject = "math"

    def __init__(self):
        self.age = 20

    # @classmethod
    # def tostring(cls):
    #     print("student class attributes: name = ", cls.name)

    @classmethod
    def tostring(cls):
        return f"student class attributes: name = {cls.name}, subject = {cls.subject}"


# one way to call the classmethod
Student.tostring()

# or you can call it this way
std = Student()
std.tostring()

# or this way
Student().tostring()

# one way to call the classmethod
print (Student.tostring())

# or you can call it this way
std = Student()
print(std.tostring())

# or this way
print(Student().tostring())


