#Code to fetch and save stock data.
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):       #define a function to fetch stock data fo a songle ticker
    data = yf.download(ticker, start=start_date, end=end_date)   #download stock data using yfinance and save it to a variable
    data.to_csv(f'{ticker}_stock_data.csv')             #save the data to a csv file with the ticker name
    return data

if __name__ == "__main__":             #runs the code if the script is run directly
    data = fetch_stock_data('AAPL', '2015-01-01', '2025-01-01')  #fetch stock data for Apple from 2015 to 2025
    print(data.head())           #print the first few rows of the data
