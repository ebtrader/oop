from main import Testapp

class Duck():
    def next(self):
        Testapp.first(self)

def main():
    app = Duck()
    app.next()

if __name__ == "__main__":
    main()

