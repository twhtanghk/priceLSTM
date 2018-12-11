# priceLSTM
Price Analysis by Long Short Term Memory

```
train model by input data.csv:
  docker run -it twhtanghk/pricelstm python model.py data.csv model.h5
predict and plot the input data based on the model
  docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD/data:/usr/src/app/data -it python plot.py model.h5 data.csv
```
