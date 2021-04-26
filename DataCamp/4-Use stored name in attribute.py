class Customer:
    def set_name(self, new_name):
        self.name = new_name

    # Using .name from the object itself
    def identify(self):
        print("I am the Customer, " + self.name)

cust = Customer()
cust.set_name("Rashid Volkov")
cust.identify()

