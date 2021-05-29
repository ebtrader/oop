class MyCompany:
    #Class Variable or Global Variable
    growth = 0.1

    def __init__(self, compname, revenue, employeesize):
        # Instance Variables
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize

print(MyCompany.growth)

