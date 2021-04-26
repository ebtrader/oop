class Customer:
    def __init__(self, name, balance=0):              # <-- set default value for balance
        self.name = name                            # <-- Create the .name attribute and set it to name parameter
        self.balance = balance                      # <-- the balance attribute added
        print("The __init__ method was called")

cust = Customer("Lara de Silva")                    # <-- don't specify balance explicitly
print(cust.name)
print(cust.balance)                                 # <-- attribute is created anyway

