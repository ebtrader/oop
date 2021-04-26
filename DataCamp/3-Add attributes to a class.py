class Customer:
    # set the name attribute of an object to new_name
    def set_name(self, new_name):
        # Create an attribute by assigning a value
        self.name = new_name    # <-- will create .name when set_name is called

cust = Customer()               # <-- .name doesn't exist here yet
cust.set_name("Lara de Silva")  # <-- .name is created and set to "Lara de Silva"
print(cust.name)                # <-- .name can be used




