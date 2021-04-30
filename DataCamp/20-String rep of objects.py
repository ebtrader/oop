class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __str__() method
    def __str__(self):
        emp_str = """
        Employee name: {name}
        Employee salary: {salary}
        """.format(name=self.name, salary=self.salary)
        return emp_str


emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
emp = Employee("Amar Howard", 40000)
print(emp)
