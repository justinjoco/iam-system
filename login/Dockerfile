FROM python:3.12-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk add --no-cache python3 postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
pip3 install -r requirements.txt && \
apk --purge del .build-deps

COPY . /usr/src/app

EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000 -k uvicorn.workers.UvicornWorker --chdir=./swagger_server run:app
