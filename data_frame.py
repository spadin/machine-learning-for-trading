import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol):
  return 'data/{}.csv'.format(symbol)

def add_symbol_to_data_frame(data_frame, symbol):
  return data_frame.join(
      get_data_frame(symbol, data_frame.index[0], data_frame.index[-1]))

def get_data_frame(symbol, start_date, end_date, dropna=False):
  date_range = pd.date_range(start_date, end_date)
  data_frame = pd.DataFrame(index = date_range)

  symbol_data_frame = pd.read_csv(symbol_to_path(symbol),
      index_col = 'Date',
      parse_dates = True,
      usecols = ['Date', 'Adj Close'],
      na_values = ['NaN'])

  symbol_data_frame = symbol_data_frame.rename(
      columns = {'Adj Close': symbol})

  data_frame = data_frame.join(symbol_data_frame)

  if(dropna == True):
    return data_frame.dropna()
  else:
    return data_frame

def spy_data_frame(start_date, end_date):
  return get_data_frame('SPY', start_date, end_date, dropna=True)

def get_data_frame_for_symbols(symbols, start_date, end_date, dropspy=False):
  df = spy_data_frame(start_date, end_date)

  for symbol in symbols:
    df = add_symbol_to_data_frame(df, symbol)

  if(dropspy == True):
    df = df.drop('SPY', axis=1)

  return df

def test_run():
  start_date = '2014-01-01'
  end_date = '2014-01-31'

  data_frame = spy_data_frame(start_date, end_date)
  data_frame.plot()
  plt.show()

if __name__ == '__main__':
  test_run()
