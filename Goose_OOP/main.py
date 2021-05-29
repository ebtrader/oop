from GooseClass import Goose

class Testapp():
    def first(self):
        numbers = [0, 1, 2, 5, 8, 15]
        for i in numbers:
            print(Goose.sum_to(i))

    def second(self):
        numbers = [20,25]
        for i in numbers:
            print(Goose.sum_to(i))



def main():
    app = Testapp()
    app.first()
    app.second()
    app.first()

if __name__ == "__main__":
    main()
