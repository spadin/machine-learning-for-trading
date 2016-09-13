import math
from data_frame import get_data_frame_for_symbols

def statistics(portfolio_value):
  daily_returns = portfolio_value.copy()
  daily_returns = (portfolio_value/portfolio_value.shift(1)) - 1
  daily_returns = daily_returns[1:]

  culmulative_return = portfolio_value.ix[-1] / portfolio_value.ix[0] - 1

  average_daily_return = daily_returns.mean()
  risk = daily_returns.std()
  sharpe_ratio = math.sqrt(252) * average_daily_return / risk

  return culmulative_return, average_daily_return, risk, sharpe_ratio

def calculate_portforlio_value(start_value, start_date, end_date, symbols, allocations):
  data_frame = get_data_frame_for_symbols(symbols, start_date, end_date, dropspy=True)
  normalized = data_frame / data_frame.ix[0]
  allocated = normalized * allocations
  position_values = start_value * allocated
  portfolio_value = position_values.sum(axis=1)

  return portfolio_value


def test_run():
  start_date = '01-01-2012'
  end_date = '12-31-2012'
  symbols = ['AAPL', 'GLD', 'GOOG', 'IBM']
  allocations = [0.4, 0.4, 0.1, 0.1]

  portfolio_value = calculate_portforlio_value(1000000, start_date, end_date, symbols, allocations)
  culmulative_return, average_daily_return, risk, sharpe_ratio = statistics(portfolio_value)

  print ''
  print 'Portfolio Value on Start Date'
  print portfolio_value[0]

  print ''
  print 'Portfolio Value on End Date'
  print portfolio_value[-1]

  print ''
  print 'Culmulative Return'
  print culmulative_return

  print ''
  print 'Average daily return'
  print average_daily_return

  print ''
  print 'Risk'
  print risk

  print ''
  print 'Sharpe Ratio'
  print sharpe_ratio

if __name__ == '__main__':
  test_run()
