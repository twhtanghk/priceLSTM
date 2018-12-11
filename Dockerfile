FROM tensorflow/tensorflow

ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN apt update \
&&  apt install -y python-tk \
&&  rm -rf /var/lib/apt/lists/* \
&&  pip install -r requirements.txt
