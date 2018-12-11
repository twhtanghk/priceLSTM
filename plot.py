# python plot.py model.h5 data.csv
import sys
from keras.models import load_model
from data import input, normalize, scaler
from env import look_back

model = load_model(sys.argv[1])

close = input(sys.argv[2])
close = scaler.fit_transform(close)
X, Y = normalize(close, look_back)

predict = scaler.inverse_transform(model.predict(X))
Y = scaler.inverse_transform(Y)

def plot(y, predict):
  import matplotlib.pyplot as plt
  plt.plot(y, label='y')
  plt.plot(predict, label='predict')
  plt.legend()
  plt.show()

plot(Y, predict)
