FROM python:3.12

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

COPY . /usr/src/app/

RUN pip install -r requirements.txt
