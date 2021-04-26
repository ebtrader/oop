starting_number = int(input("What is the starting number? "))
number_increment = int(input("What is the number increment? "))
class MyCounter:
    def set_count(self, n):
        self.count = n
mc = MyCounter()
mc.set_count(starting_number)
mc.count = mc.count + number_increment
print(mc.count)

