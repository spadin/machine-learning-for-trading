from data_frame import get_data_frame_for_symbols
import matplotlib.pyplot as plt

def compute_daily_returns(data_frame):
  daily_returns = data_frame.copy()
  daily_returns = (daily_returns/daily_returns.shift(1)) - 1
  daily_returns.ix[0,:] = 0
  return daily_returns

def test_run():
  start_date = '2012-01-01'
  end_date = '2012-12-31'

  data_frame = get_data_frame_for_symbols(['GLD'], start_date, end_date)

  daily_returns = compute_daily_returns(data_frame)
  ax = daily_returns.plot()

  ax.set_xlabel('Date')
  ax.set_ylabel('Price')
  ax.legend(loc='upper left')

  plt.show()

if __name__ == '__main__':
  test_run()
