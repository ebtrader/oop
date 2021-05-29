class MyCompany:
    def __init__(self, compname, revenue, employeesize):
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize

    def productivity(self):
        return self.revenue/self.no_of_employees

company1 = MyCompany('XYZBank', 1000, 100)
print(company1.productivity())

company2=MyCompany('ABCBank', 5000, 200)
print(company2.productivity())

