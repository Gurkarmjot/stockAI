#Code to fetch and save stock data.
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):       #define a function to fetch stock data
    data = yf.download(ticker, start=start_date, end=end_date)   
    data.to_csv(f'{ticker}_stock_data.csv')
    return data

if __name__ == "__main__":
    data = fetch_stock_data('AAPL', '2015-01-01', '2025-01-01')
    print(data.head())
