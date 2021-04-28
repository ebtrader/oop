class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

# Empty class inherited from BankAccount
class SavingsAccount(BankAccount):
    # Constructor specifically for SavingsAccount with an additional parameter
    def __init__(self, balance, interest_rate):
        # Call the parent constructor using ClassName.__init__()
        BankAccount.__init__(self, balance)     #<--- self is a SavingsAccount but also a BankAccount
        # Add more functionality
        self.interest_rate = interest_rate

    def compute_interest(self, n_periods = 1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)

acct = SavingsAccount(1000, 0.03)
print(acct.interest_rate)

print(acct.compute_interest(2))


