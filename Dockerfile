FROM tensorflow/tensorflow

ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN pip install -r requirements.txt
