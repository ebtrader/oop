class Customer:
    def __init__(self, name, balance):              # <-- balance parameter added
        self.name = name                            # <-- Create the .name attribute and set it to name parameter
        self.balance = balance                      # <-- the balance attribute added
        print("The __init__ method was called")

cust = Customer("Lara de Silva", 1000)
print(cust.name)
print(cust.balance)


