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

class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount, fee=0):
        if fee <= self.limit:
            BankAccount.withdraw(self, amount - fee)
        else:
            BankAccount.withdraw(self, amount - self.limit)
        self.balance -= amount

acct = SavingsAccount(1000, 0.03)
print(acct.interest_rate)

print(acct.compute_interest(2))

check_acct = CheckingAccount(1000, 25)

#check_acct.deposit(100)
#print(check_acct.balance)

check_acct.withdraw(300,5)
print(check_acct.balance)