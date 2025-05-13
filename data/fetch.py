import os
import yfinance as yf # type: ignore
import pandas as pd
import csv

def fetch_sp500_companies():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_df = pd.read_html(url)[0]
    sp500_list = sp500_df['Symbol'].tolist()
    sp500_list = [t.replace('.', '-') for t in sp500_list]
    return sp500_list

def fetch_nasdaq100_companies():
    url = "https://en.wikipedia.org/wiki/NASDAQ-100"
    tables = pd.read_html(url)
    nasdaq100_df = tables[4]
    nasdaq100_list = nasdaq100_df['Ticker'].tolist()
    nasdaq100_list = [t.replace('.', '-') for t in nasdaq100_list]
    return nasdaq100_list

def fetch_stock_data(company, start_date, end_date, interval = "1d"):
    directory = f"{interval}_{start_date}_to_{end_date}"
    os.makedirs(f"data/{directory}", exist_ok=1)
    file_name = f"data/{directory}/{company}.csv"
    
    
    data = yf.download(company, start=start_date, end=end_date, interval=interval)
    
    print(data)
    print(type(data))

    data.to_csv(file_name, index="false")
    
    return data



if __name__ == "__main__":
    companies = ["SPY"]
    for company in companies:
        fetch_stock_data(company=company, start_date='2001-11-26', end_date='2007-11-14', interval="1d")
