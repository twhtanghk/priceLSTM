FROM tensorflow/tensorflow

ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN apt update \
&&  apt install python-tk \
&&  pip install -r requirements.txt
