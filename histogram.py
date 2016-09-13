from data_frame import get_data_frame
from daily_returns import compute_daily_returns
import matplotlib.pyplot as plt

def test_run():
  start_date = '2012-01-01'
  end_date = '2012-12-31'
  symbol = 'AAPL'

  data_frame = get_data_frame(symbol, start_date, end_date)
  daily_returns = compute_daily_returns(data_frame)

  daily_returns.hist(bins=20)

  mean = daily_returns[symbol].mean()
  std = daily_returns[symbol].std()

  plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
  plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
  plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)

  plt.show()

if __name__ == '__main__':
  test_run()
