#pull official base image
FROM python:3.8.0-slim-buster

#Set work directory
WORKDIR /usr/src/app

#set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/

#install dependencies

RUN pip install --upgrade pip
RUN pip install -r requirements.txt