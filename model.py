# python model.py data.csv model.h5
import sys
from data import input, scaler, normalize
from env import look_back

close = input(sys.argv[1])
close = scaler.fit_transform(close)
X, Y = normalize(close, look_back)

from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X, Y, epochs=len(X), batch_size=1, verbose=2)

model.save(sys.argv[2])
