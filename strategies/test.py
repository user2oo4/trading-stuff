import utils

file_path = 'data/1d_2023-01-01_to_2024-01-01/AAPL.csv'
data_dict = utils.get_data(file_path)
sharpe_ratio = utils.sharpe_ratio(data_dict=data_dict, riskfree_rate=0.04, Nt=252)
print(sharpe_ratio)