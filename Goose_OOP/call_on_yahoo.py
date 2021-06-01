import yfinance as yf
import pandas as pd
from yahoo_download_loop import Yahoo
from main_on_main import Duck

class Test:

    def duck(self):
        Yahoo.historical(self)

    def call_on_main(self):
        Duck.next(self)

def main():
    app = Test()
    app.duck()
    app.call_on_main()

if __name__ == "__main__":
    main()
