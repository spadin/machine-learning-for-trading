import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo
import numpy as np

def f(line, data):
  # Both of these return the same results.
  # return np.sum((data.ix[:, 1] - (line[0] * data.ix[:, 0] + line[1])) ** 2)

  # This version works with higher-order polynomial.
  return np.sum((data.ix[:, 1] - np.polyval(line, data.ix[:, 0])) ** 2)

def test_run():
  data = pd.DataFrame({
    'x': pd.Series([1, 2, 3, 4, 5]),
    'y': pd.Series([1, 2, 3, 5, 5]),
  })

  data.plot(kind='scatter', x=0, y=1)

  guess = np.float32([2,0])

  result = spo.minimize(f, guess, args=(data,), method='SLSQP')
  m, c = result.x

  x1 = 0
  y1 = m*x1 + c

  x2 = 5.0
  y2 = m*x2 + c

  plt.plot([x1, x2], [y1, y2], color='k', linestyle='-', linewidth=1)

  plt.show()


if __name__ == '__main__':
  test_run()
