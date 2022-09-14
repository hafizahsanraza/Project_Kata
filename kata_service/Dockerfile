FROM python:3.10.4-slim-buster

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
build-essential gcc

WORKDIR /app

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app


EXPOSE 80

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "app:get_app()", "--worker-class", "aiohttp.GunicornWebWorker" ]