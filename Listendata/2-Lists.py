class MyClass:
    def __init__(self, name):
        self.name = name
        self.pretty_print_name()

    def pretty_print_name(self):
        print("this object's name is {}.".format(self.name))

my_objects = {}

for i in range(1,11):
    name = 'obj_{}'.format(i)
