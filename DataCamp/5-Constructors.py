class Customer:
    def __init__(self, name):
        self.name = name                            # <-- Create the .name attribute and set it to name parameter
        print("The __init__ method was called")

cust = Customer("Lara de Silva")                    # <-- __init__ is implicitly called
print(cust.name)


