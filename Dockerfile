FROM python:alpine

WORKDIR /usr/src/app
RUN apk add --no-cache git
RUN pip install --no-cache-dir gunicorn git+https://github.com/hcv57/coinrankchat-telegram#egg=coinrankchat_telegram
COPY ./noavatar.jpeg .
CMD python -m coinrankchat.telegram