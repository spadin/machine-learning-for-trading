import math
from datetime import datetime
from data_frame import get_data_frame_for_symbols

def statistics(portfolio_value, sampling_frequency, risk_free_return):
  daily_returns = portfolio_value.copy()
  daily_returns = (portfolio_value/portfolio_value.shift(1)) - 1
  daily_returns = daily_returns[1:]

  culmulative_return = portfolio_value.ix[-1] / portfolio_value.ix[0] - 1

  average_daily_return = daily_returns.mean()
  standard_deviation_of_daily_returns = daily_returns.std()
  sharpe_ratio = math.sqrt(sampling_frequency) * ( average_daily_return - risk_free_return ) / standard_deviation_of_daily_returns

  return culmulative_return, average_daily_return, standard_deviation_of_daily_returns, sharpe_ratio

def calculate_portforlio_value(start_value, start_date, end_date, symbols, allocations):
  data_frame = get_data_frame_for_symbols(symbols, start_date, end_date, dropspy=True)
  normalized = data_frame / data_frame.ix[0]
  allocated = normalized * allocations
  position_values = start_value * allocated
  portfolio_value = position_values.sum(axis=1)

  return portfolio_value

def assess_portfolio(start_value, start_date, end_date,
                     symbols, allocations, risk_free_return=0.0,
                     sampling_frequency=252):

  portfolio_value = calculate_portforlio_value(1000000, start_date, end_date,
                                               symbols, allocations)
  end_value = portfolio_value[-1]
  culmulative_return, average_daily_return, standard_deviation_of_daily_returns, sharpe_ratio = statistics(portfolio_value, sampling_frequency, risk_free_return)

  return culmulative_return, average_daily_return, standard_deviation_of_daily_returns, sharpe_ratio, end_value

def test_run():
  start_date = datetime(2012, 1, 1)
  end_date = datetime(2013, 1, 1)
  symbols = ['AAPL', 'GLD', 'GOOG', 'IBM']
  allocations = [0.4, 0.4, 0.1, 0.1]
  start_value = 1000000

  portfolio_value = calculate_portforlio_value(start_value, start_date, end_date, symbols, allocations)
  culmulative_return, average_daily_return, standard_deviation_of_daily_returns, sharpe_ratio, end_value = assess_portfolio(1000000, start_date, end_date, symbols, allocations)

  print ''
  print 'Portfolio Value on Start Date'
  print start_value

  print ''
  print 'Portfolio Value on End Date'
  print end_value

  print ''
  print 'Culmulative Return'
  print culmulative_return

  print ''
  print 'Average daily return'
  print average_daily_return

  print ''
  print 'Standard deviation of daily returns'
  print standard_deviation_of_daily_returns

  print ''
  print 'Sharpe Ratio'
  print sharpe_ratio

if __name__ == '__main__':
  test_run()
