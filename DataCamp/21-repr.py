class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    def __repr__(self):
        s = "Employee('{name}', {salary})".format(name=self.name, salary=self.salary)
        return s

    # Add the __repr__method


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))
emp = Employee("Amar Howard", 40000)
print(emp)