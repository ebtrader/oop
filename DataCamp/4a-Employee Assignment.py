class Employee:

    def set_name(self, new_name):
        self.name = new_name

    # Add set_salary() method
    def set_salary(self, new_salary):
        self.salary = new_salary

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self, divisor):
        return self.salary / divisor

# Create an object emp of class Employee
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)

# set the raise
emp.give_raise(1500)

# print the new salary including the raise
print(emp.salary)

# Get monthly salary of emp and assign to mon_sal
monthly = emp.monthly_salary(12)
print(monthly)
# pass the monthly salary to mon_sal
mon_sal = emp.salary

# Print mon_sal
print (mon_sal)