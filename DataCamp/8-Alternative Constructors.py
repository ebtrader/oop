class Employee:
    # Define a class attribute
    MIN_SALARY = 30000      #<-- no self.
    def __init__(self, name, salary=30000):
        self.name = name
        # Use class name to access class attribute
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.readline()
        return cls(name)

emp = Employee.from_file("employee_data.txt")
type(emp)