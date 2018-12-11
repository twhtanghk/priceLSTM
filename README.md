# priceLSTM
Price Analysis by Long Short Term Memory

```
train model by input data.csv and save the model:
  docker run -v $PWD/data:/usr/src/app/data -it twhtanghk/pricelstm python model.py data/data.csv data/model.h5
predict and plot the input data based on the model
  docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD/data:/usr/src/app/data -it twhtanghk/pricelstm python plot.py data/model.h5 data/data.csv
```
