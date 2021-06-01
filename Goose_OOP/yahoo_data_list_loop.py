import yfinance as yf
import pandas as pd

class Yahoo_data:

    def historical(self, tickers):
        #tickers = ['NQ=F', 'ES=F']
        for i in tickers:
            data = yf.download(tickers=i, period='1y')
            self.df = pd.DataFrame(data)
            print(self.df)

    def convert(self):
        self.df.to_csv('tickers.csv')

def main():
    app = Yahoo_data()
    tickers = ['SPY', 'QQQ']
    app.historical(tickers)
    app.convert()

if __name__ == "__main__":
    main()

