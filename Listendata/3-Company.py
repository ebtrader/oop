#Create company class

class Company:

    # attributes
    name = 'XYZ Bank'
    turnover = 5000
    revenue = 1000
    no_of_employees = 100

    # method
    def productivity(self):
        return Company.revenue/Company.no_of_employees

print(Company.name)
print(Company.turnover)
print(Company.no_of_employees)
print(Company().productivity())

Bank = 