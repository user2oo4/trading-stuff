import csv
import statistics
import math

def get_data(file_path):
    data_dict = {}

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        next(reader)
        
        for row in reader:
            date = row['Date']
            if not date:
                continue

            # print("date = ", date)
            # print("row = ", row)
            
            data_dict[date] = {
                'Close': float(row['Close']),
                'High': float(row['High']),
                'Low': float(row['Low']),
                'Open': float(row['Open']),
                'Volume': int(row['Volume']),
            }
    return data_dict

def sharpe_ratio(data_dict, riskfree_rate = 0.04, Nt = 252):
    # data_dict: Should contain data dictionary
    # with time being key and a dictionary of prices
    # Nt: number of periods in year (default value is trading days in a year)
    daily_ret_array = []
    riskfree_rate = riskfree_rate / Nt
    # print("Risk free rate:", riskfree_rate)
    for time in data_dict:
        data = data_dict[time]
        daily_return = (data['Close'] - data['Open']) / data['Open']
        excess_daily_return = daily_return - riskfree_rate
        data['Dailyret'] = daily_return
        data['Excess-Dailyret'] = excess_daily_return
        daily_ret_array.append(excess_daily_return)
    # print(daily_ret_array)
    mean = statistics.mean(daily_ret_array)
    stddev = statistics.stdev(daily_ret_array)
    # print("mean:", mean)
    # print("stddev:", stddev)
    ans = math.sqrt(Nt) * mean / stddev
    return ans
