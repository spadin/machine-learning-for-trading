from data_frame import get_data_frame_for_symbols
from daily_returns import compute_daily_returns
import matplotlib.pyplot as plt
import numpy as np

def test_run():
  start_date = '2014-01-01'
  end_date = '2014-12-31'
  symbols = ['IBM', 'GLD']

  data_frame = get_data_frame_for_symbols(symbols, start_date, end_date)
  daily_returns = compute_daily_returns(data_frame)

  daily_returns.plot(kind='scatter', x='SPY', y=symbols[0])

  beta_0, alpha_0 = np.polyfit(daily_returns['SPY'], daily_returns[symbols[0]], 1)
  plt.plot(daily_returns['SPY'], beta_0*daily_returns['SPY'] + alpha_0, '-', color='r')


  daily_returns.plot(kind='scatter', x='SPY', y=symbols[1])

  beta_1, alpha_1 = np.polyfit(daily_returns['SPY'], daily_returns[symbols[1]], 1)
  plt.plot(daily_returns['SPY'], beta_1*daily_returns['SPY'] + alpha_1, '-', color='r')

  plt.show()

  print daily_returns.corr(method='pearson')

if __name__ == '__main__':
  test_run()
