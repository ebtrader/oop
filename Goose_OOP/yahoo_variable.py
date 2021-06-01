import yfinance as yf
import pandas as pd

class Yahoo:
    def historical(self, tickers):
        self.tickers = tickers
        for i in self.tickers:
            data = yf.download(i, period='1y')
            df = pd.DataFrame(data)
            print(df)
            df.to_csv(i + '.csv')


def main():
    app = Yahoo()
    tickers = ['SPY', 'IBM']
    app.historical(tickers)


if __name__ == "__main__":
    main()