class Customer:
    #define a method called identify that takes self and name as a parameter
    def identify(self, name):
        # the method prints the following when called
        print("I am the Customer, " + name)

# create a new customer object
cust = Customer()
# call the method by using the object.method syntax
# pass the desired name into the method
cust.identify("Laura")
# is same as
Customer.identify(cust, "Laura")

