from data_frame import get_data_frame
import pandas as pd
import matplotlib.pyplot as plt
import getopt
import sys

def bollinger_bands(rolling_mean, rolling_std):
  upper_band = rolling_mean + rolling_std * 2
  lower_band = rolling_mean - rolling_std * 2

  return upper_band, lower_band

def rolling_std(data_frame, symbol, window=20):
  return data_frame[symbol].rolling(window, center=False).std()

def rolling_mean(data_frame, symbol, window=20):
  return data_frame[symbol].rolling(window, center=False).mean()

def options():
  start_date = '2012-01-01'
  end_date = '2012-09-30'
  symbol = 'SPY'
  window = 20

  options, remainder = getopt.getopt(
      sys.argv[1:], '', [
        'start_date=', 'end_date=',
        'symbol=', 'window='])

  for opt, arg in options:
    if opt in ('--start_date'):
      start_date = arg
    elif opt in ('--end_date'):
      end_date = arg
    elif opt in ('--symbol'):
      symbol = arg
    elif opt in ('--window'):
      window = int(arg)

  return start_date, end_date, symbol, window

def test_run():
  start_date, end_date, symbol, window = options()

  data_frame = get_data_frame(symbol, start_date, end_date, dropna=True)
  ax = data_frame.plot(title='Bollinger bands', label=symbol)

  rm = rolling_mean(data_frame, symbol, window = window)
  rm.plot(label='Rolling mean', ax=ax)

  rstd = rolling_std(data_frame, symbol, window = window)

  upper_band, lower_band = bollinger_bands(rm, rstd)

  upper_band.plot(label='Upper band', ax=ax)
  lower_band.plot(label='Lower band', ax=ax)

  plt.legend(loc='upper left')
  plt.show()

if __name__ == '__main__':
  test_run()
