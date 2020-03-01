FROM python:3.7

WORKDIR /app

ENV APP_KEY = 123

COPY requirements.txt /app

RUN pip install -r requirements.txt