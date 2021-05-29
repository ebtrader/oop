class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name

    @classmethod
    def getobject(cls):
        return cls(20000, 'jerry')

    def use_the_cl(self):
        return Employee.getobject().salary*2

emp1 = Employee(10000, "john doe")
print(emp1.salary)
print(emp1.name)

emp2 = Employee.getobject()
print(emp2.salary)
print(emp2.name)

print(emp2.use_the_cl())


