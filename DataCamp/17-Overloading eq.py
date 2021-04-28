class Customer:
    def __init__(self, id, name):
        self.id, self.name = id, name
    # Will be called when == is used
    def __eq__(self, other):
        # Diagnostic printout
        print("__eq__() is called")

        # Returns True if all attributes match
        return (self.id == other.id) and (self.name == other.name)

# Two equal objects

customer1 = Customer(123, "Maryam Azar")
customer2 = Customer(123, "Maryam Azar")

print(customer1 == customer2)
