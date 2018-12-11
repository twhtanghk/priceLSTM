def input(file):
  import pandas as pd
  df = pd.read_csv(file)
  df = df.sort_values('date')
  high = df.loc[:, 'high'].values
  low = df.loc[:, 'low'].values
  mid = (high + low) / 2.0
  close = df.loc[:, 'close']
  return close.values.reshape(-1, 1)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

def normalize(dataset, look_back=1):
  import numpy
  X, Y = [], []
  for i in range(len(dataset) - look_back):
    a = dataset[i:(i + look_back)]
    X.append(a)
    Y.append(dataset[i + look_back])
  X, Y = numpy.array(X), numpy.array(Y)
  X = numpy.reshape(X, (X.shape[0], 1, X.shape[1]))
  return X, Y
