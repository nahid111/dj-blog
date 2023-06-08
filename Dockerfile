# pull official base image
FROM python:3.11.3-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -y
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential

# set work directory
WORKDIR /usr/src/app
RUN mkdir /usr/src/app/staticfiles

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy source_files to work_dir
COPY . .
