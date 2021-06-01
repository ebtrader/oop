import yfinance as yf
import pandas as pd
from yahoo_download_loop import Yahoo

class Test():
    def duck(self):
        tickers = ['QQQ', 'SPY']
        Yahoo.historical(self)

def main():
    app = Test()

    app.duck()

if __name__ == "__main__":
    main()
