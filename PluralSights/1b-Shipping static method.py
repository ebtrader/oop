from shipping import *

class ShippingContainer:

    next_serial = 1337                              # class attribute

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code                # instance attribute
        self.contents = contents                    # instance attribute
        self.serial = ShippingContainer._generate_serial()
        #self.serial = ShippingContainer.next_serial # class attribute
        #ShippingContainer.next_serial += 1          # augmented assignment modifies class attribute in place


c1 = ShippingContainer("YML", ["books"])

print(c1.owner_code)
print(c1.contents)

c2 = ShippingContainer("MAE", ["clothes"])

print(c2.owner_code)
print(c2.contents)

c3 = ShippingContainer("MAE", ["tools"])
print(c3.serial)

c4 = ShippingContainer("ESC", ["electronics"])
print(c4.serial)

c5 = ShippingContainer("ESC", ["pharma"])
print(c5.serial)

c6 = ShippingContainer("ESC", ["noodles"])
print(c6.serial)

print(ShippingContainer.next_serial)
print(c5.next_serial)
print(c6.next_serial)

print(ShippingContainer.next_serial)


