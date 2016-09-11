from data_frame import get_data_frame
import pandas as pd
import matplotlib.pyplot as plt

def compute_culmulative_returns(data_frame):
  culmulative_returns = data_frame.copy()
  culmulative_returns = (data_frame/data_frame.ix[0,:].values) - 1
  return culmulative_returns

def test_run():
  start_date = '2012-01-01'
  end_date = '2012-12-31'
  symbol = 'AAPL'

  data_frame = get_data_frame(symbol, start_date, end_date, dropna=True)
  ax = data_frame.plot(title='Daily Adj Close')
  ax.set_xlabel('Date')
  ax.set_ylabel('Price')

  culmulative_returns = compute_culmulative_returns(data_frame)
  ax = culmulative_returns.plot(title='Culmulative returns', label='Culmulative returns')
  ax.set_xlabel('Date')
  ax.set_ylabel('Price')

  plt.legend(loc='upper left')
  plt.show()

if __name__ == '__main__':
  test_run()
