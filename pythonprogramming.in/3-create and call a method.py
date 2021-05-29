class Employee:
    salary = 10000
    name = "John Doe"

    def tax(self):
        print(self.salary * 0.10)

emp1 = Employee()
print(emp1.salary)
print(emp1.name)
emp1.tax()

